# 🚨 Dew-Based Federated Learning for Disaster-Resilient Networks

## 📌 Overview
This project presents a **Dew-Based Federated Learning (DFL)** framework designed for real-time disaster detection and alert generation in environments with limited or no internet connectivity. The system enables **on-device intelligence**, **privacy-preserving learning**, and **offline communication**, making it suitable for disaster-prone and infrastructure-limited regions.

---

## 🏗️ System Architecture

The system follows a **three-layer hierarchical architecture**:

### 🔹 Dew Layer
- Local devices (smartphones, CCTV, IoT sensors)
- Performs:
  - Image capture
  - CNN-based disaster detection
  - Local alert generation
  - On-device training

### 🔹 Fog Layer
- Edge servers / routers
- Performs:
  - Federated model aggregation (FedAvg)
  - Device coordination
  - Local network management

### 🔹 Cloud Layer
- Central monitoring system
- Performs:
  - Global model update
  - Data storage
  - Dashboard visualization (Streamlit)

---

## 🚀 Key Features

- ✅ Real-time disaster detection  
- ✅ Offline operation (no internet required)  
- ✅ Federated learning (no raw data sharing)  
- ✅ Privacy-preserving architecture  
- ✅ Low-latency inference (<100 ms)  
- ✅ Location-based alert system (Latitude, Longitude, City)  
- ✅ Streamlit dashboard for monitoring  

---

## 🧠 Model Details

- Lightweight **Convolutional Neural Network (CNN)**
- Input: 224 × 224 RGB images  
- Output: 9 disaster categories  
- Framework: PyTorch  
- Federated Learning: Flower (FedAvg)

---

## 📊 Performance

| Metric     | Value |
|------------|------|
| Accuracy   | 94.8% |
| Precision  | 94.1% |
| Recall     | 94.3% |
| F1-Score   | 94.2% |

---

## ⚙️ Technologies Used

- Python  
- PyTorch  
- Flower (Federated Learning)  
- Streamlit  
- Flask  
- MQTT  
- OpenCV  

---

## 📂 Project Structure
