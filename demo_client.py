import requests
import time
from math import radians, cos, sin, sqrt, atan2

BASE_URL = "http://127.0.0.1:5000"

def haversine(lat1, lon1, lat2, lon2):
    """Return distance in km between two lat/lon points."""
    R = 6371.0
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi, dlambda = radians(lat2 - lat1), radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1) * cos(phi2) * sin(dlambda/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1-a))

def register_user(name, lat, lon, is_volunteer):
    response = requests.post(f"{BASE_URL}/register", json={
        "name": name,
        "lat": lat,
        "lon": lon,
        "is_volunteer": is_volunteer
    })
    return response.json()

def trigger_sos(name, lat, lon):
    response = requests.post(f"{BASE_URL}/sos", json={
        "name": name,
        "lat": lat,
        "lon": lon
    })
    return response.json()

def view_alerts():
    response = requests.get(f"{BASE_URL}/view_alerts")
    return response.json()

# ------------------ Demo Setup ------------------

# Step 1: Register volunteers and users
users = [
    {"name": "Alice", "lat": 28.6139, "lon": 77.2090, "is_volunteer": 1},
    {"name": "Bob", "lat": 28.6200, "lon": 77.2100, "is_volunteer": 1},
    {"name": "Priya", "lat": 28.6150, "lon": 77.2120, "is_volunteer": 0},
    {"name": "Meera", "lat": 28.6180, "lon": 77.2150, "is_volunteer": 0}
]

print("\n--- Registering Users ---")
for u in users:
    res = register_user(u["name"], u["lat"], u["lon"], u["is_volunteer"])
    print(f"Registered {u['name']} -> {res}")

time.sleep(1)

# Step 2: Trigger multiple SOS alerts
sos_events = [
    {"name": "Priya", "lat": 28.6150, "lon": 77.2120},
    {"name": "Meera", "lat": 28.6180, "lon": 77.2150}
]

print("\n--- Triggering SOS Alerts ---")
for sos in sos_events:
    res = trigger_sos(sos["name"], sos["lat"], sos["lon"])
    print(f"SOS by {sos['name']} -> {res}")
    # Calculate distances to volunteers manually for demonstration
    for v in [u for u in users if u["is_volunteer"] == 1]:
        dist = haversine(sos["lat"], sos["lon"], v["lat"], v["lon"])
        if dist <= 3.0:
            print(f" -> Volunteer {v['name']} alerted (distance {dist:.2f} km)")
    print()
    time.sleep(1)

# Step 3: View all alerts
print("\n--- All SOS Alerts ---")
alerts = view_alerts()
for alert in alerts:
    ts_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(alert["timestamp"]))
    print(f"{alert['name']} at ({alert['lat']}, {alert['lon']}) -> {ts_readable}")
