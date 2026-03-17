from flask import Flask, request, jsonify
import sqlite3
import time
import math

app = Flask(__name__)
DB = "safezone.db"

# ---------- DB / Utils ----------
def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lat REAL,
                lon REAL,
                is_volunteer INTEGER
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS sos_alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lat REAL,
                lon REAL,
                timestamp INTEGER
            )
        ''')
        conn.commit()

def haversine(lat1, lon1, lat2, lon2):
    """
    Return distance in kilometers between two lat/lon points.
    """
    R = 6371.0  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# ---------- API Routes ----------
@app.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    name = data.get('name')
    lat = float(data.get('lat'))
    lon = float(data.get('lon'))
    is_volunteer = int(data.get('is_volunteer', 0))

    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute(
            'INSERT INTO users (name, lat, lon, is_volunteer) VALUES (?, ?, ?, ?)',
            (name, lat, lon, is_volunteer)
        )
        conn.commit()
        user_id = c.lastrowid

    return jsonify({"status": "registered", "user_id": user_id}), 201

@app.route('/sos', methods=['POST'])
def sos():
    data = request.json or {}
    name = data.get('name', 'unknown')
    lat = float(data.get('lat'))
    lon = float(data.get('lon'))
    timestamp = int(time.time())

    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute(
            'INSERT INTO sos_alerts (name, lat, lon, timestamp) VALUES (?, ?, ?, ?)',
            (name, lat, lon, timestamp)
        )
        conn.commit()
        sos_id = c.lastrowid

    radius_km = 3.0  # 3 km radius for volunteer notification
    volunteers_alerted = []

    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('SELECT name, lat, lon FROM users WHERE is_volunteer=1')
        rows = c.fetchall()

    for vname, vlat, vlon in rows:
        if vlat is None or vlon is None:
            continue
        dist = haversine(lat, lon, vlat, vlon)
        if dist <= radius_km:
            volunteers_alerted.append({'name': vname, 'distance_km': round(dist, 3)})
            print(f"[NOTIFY] Volunteer '{vname}' ~{dist:.3f} km from SOS at {lat},{lon}")

    response = {
        "status": "sos_triggered",
        "sos_id": sos_id,
        "location": {"lat": lat, "lon": lon},
        "volunteers_alerted": volunteers_alerted
    }
    return jsonify(response), 201

@app.route('/view_alerts', methods=['GET'])
def view_alerts():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('SELECT id, name, lat, lon, timestamp FROM sos_alerts ORDER BY id DESC')
        rows = c.fetchall()

    alerts = []
    for r in rows:
        alerts.append({
            'id': r[0],
            'name': r[1],
            'lat': r[2],
            'lon': r[3],
            'timestamp': r[4]
        })
    return jsonify(alerts)
# ---------- Main ----------
if __name__ == '__main__':
    init_db()
    print("SafeNet server starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

