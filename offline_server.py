from flask import Flask, request, jsonify
import base64
import os
from datetime import datetime

app = Flask(__name__)

# create folders
os.makedirs("images", exist_ok=True)
os.makedirs("logs", exist_ok=True)

@app.route("/receive_alert", methods=["POST"])
def receive_alert():
    try:
        data = request.json

        timestamp = data.get("timestamp", datetime.now().strftime("%H:%M:%S"))
        image_base64 = data.get("image")

        lat = data.get("latitude", "NA")
        lon = data.get("longitude", "NA")
        location_name = data.get("location_name", "Unknown")

        # =============================
        # SAVE IMAGE (UNIQUE NAME)
        # =============================
        filename = None
        if image_base64:
            image_data = base64.b64decode(image_base64)
            filename = f"images/alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

            with open(filename, "wb") as f:
                f.write(image_data)

        # =============================
        # SAVE LOG
        # =============================
        log_entry = (
            f"{timestamp} | ALERT | {location_name} | "
            f"Lat:{lat}, Lon:{lon} | Image:{filename}\n"
        )

        with open("logs/alerts.log", "a") as f:
            f.write(log_entry)

        print("✅ Alert Received:", log_entry)

        return jsonify({"status": "success"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)