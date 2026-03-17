# client_sim.py
import requests, time

SERVER = "http://127.0.0.1:5000"

def register_user(name, lat, lon, is_volunteer=0):
    payload = {"name": name, "lat": lat, "lon": lon, "is_volunteer": is_volunteer}
    r = requests.post(f"{SERVER}/register", json=payload)
    print("Register:", name, "->", r.status_code, r.json())
    return r.json().get('user_id')

def trigger_sos(name, lat, lon):
    payload = {"name": name, "lat": lat, "lon": lon}
    r = requests.post(f"{SERVER}/sos", json=payload)
    print("SOS response ->", r.status_code)
    print(r.json())
    return r.json()

if __name__ == "__main__":
    # Register demo volunteers (locations chosen close to demo SOS)
    volunteers = [
        ("Asha", 12.9716, 77.5946, 1),
        ("Riya", 12.9720, 77.5938, 1),
        ("Priya", 12.9850, 77.6000, 1),  # a bit farther
    ]
    for name, lat, lon, is_vol in volunteers:
        register_user(name, lat, lon, is_vol)
        time.sleep(0.2)

    # Register a normal user (not volunteer)
    register_user("Meera", 12.9719, 77.5940, 0)

    print("\n--- Simulating SOS from Meera ---\n")
    time.sleep(1)
    trigger_sos("Meera", 12.9719, 77.5940)
