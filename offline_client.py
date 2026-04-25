import requests
from datetime import datetime

# =============================
# SETTINGS
# =============================
SERVER_IP = "127.0.0.1"   # 👉 change to 192.168.137.1 for mobile
BASE_URL = f"http://{SERVER_IP}:5000"

# =============================
# REGISTER DEVICE
# =============================
def register_device():
    try:
        response = requests.post(f"{BASE_URL}/register")
        print("✅ Registered with server:", response.json())
    except Exception as e:
        print("⚠ Registration failed:", e)

# =============================
# SEND ALERT
# =============================
def send_alert():
    data = {
        "disaster": "Flood",
        "human_detected": True,
        "timestamp": datetime.now().strftime("%H-%M-%S")
    }

    try:
        response = requests.post(f"{BASE_URL}/receive_alert", json=data)
        print("🚨 Alert sent:", response.json())
    except Exception as e:
        print("❌ Failed to send alert:", e)

# =============================
# MAIN
# =============================
if __name__ == "__main__":
    register_device()
    send_alert()