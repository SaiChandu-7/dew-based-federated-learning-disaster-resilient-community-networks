import streamlit as st
import os
import time

st.set_page_config(page_title="Disaster Monitoring", layout="wide")

st.title("🚨 Real-Time Disaster Monitoring Dashboard")

log_file = "logs/alerts.log"
image_folder = "images"

placeholder = st.empty()

while True:
    with placeholder.container():

        col1, col2 = st.columns(2)

        # =============================
        # LEFT SIDE: ALERT LOGS
        # =============================
        with col1:
            st.subheader("📊 Latest Alerts")

            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    logs = f.readlines()

                if logs:
                    for log in reversed(logs[-5:]):
                        st.write(log)
                else:
                    st.write("No alerts yet.")
            else:
                st.write("No log file found.")

        # =============================
        # RIGHT SIDE: IMAGE DISPLAY
        # =============================
        with col2:
            st.subheader("🖼 Latest Image")

            if os.path.exists(image_folder):
                images = sorted(
                    os.listdir(image_folder),
                    key=lambda x: os.path.getmtime(os.path.join(image_folder, x)),
                    reverse=True
                )

                if images:
                    latest_image = os.path.join(image_folder, images[0])
                    st.image(latest_image, use_column_width=True)
                else:
                    st.write("No images found.")
            else:
                st.write("Image folder not found.")

        st.markdown("---")
        st.success("System Running (Offline Mode Enabled)")

    time.sleep(2)
    st.rerun()