import requests

BASE_URL = "http://127.0.0.1:5000"

# 1️⃣ Register users
users = [
    {"name": "Alice", "lat": 28.6139, "lon": 77.2090, "is_volunteer": 1},
    {"name": "Bob", "lat": 28.6200, "lon": 77.2100, "is_volunteer": 1},
    {"name": "Priya", "lat": 28.6150, "lon": 77.2120, "is_volunteer": 0}
]

for u in users:
    response = requests.post(f"{BASE_URL}/register", json=u)
    print("Register Response:", response.json())

# 2️⃣ Trigger SOS
sos_data = {"name": "Priya", "lat": 28.6150, "lon": 77.2120}
response = requests.post(f"{BASE_URL}/sos", json=sos_data)
print("\nSOS Response:", response.json())

# 3️⃣ View all SOS alerts
response = requests.get(f"{BASE_URL}/view_alerts")
print("\nAll SOS Alerts:", response.json())
