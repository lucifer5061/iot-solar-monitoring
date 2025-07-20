# ☀️ IoT-Enabled Remote Monitoring and Predictive Maintenance of Solar Panels

This project is a fully simulated IoT system designed to remotely monitor solar panel performance and predict optimal cleaning intervals using a machine learning model. The system helps improve energy yield and reduce manual maintenance by integrating smart data-driven decisions into solar panel upkeep.

---

## 🔧 Features

- **Real-time Monitoring Dashboard** (Node-RED)
  - Voltage, Current, Temperature, Irradiance, Dust Level
  - Visual trends and live telemetry

- **Next Cleaning Prediction Widget**
  - Dynamically predicts the number of days left until panel cleaning is required
  - Highlights when cleaning is urgent (≤ 5 days)

- **Email Alert System**
  - Automatically sends notifications to the system owner or cleaner when panel performance is degrading due to dust accumulation

- **Machine Learning Integration**
  - Python-based ML model for predictive maintenance
  - Trained using synthetic data to simulate real-world performance trends

- **MQTT Communication**
  - All sensor data is simulated and transmitted using the MQTT protocol for real-time interaction with Node-RED


---

## 🚀 How It Works

1. **Simulated sensor data** is published via MQTT using `mqtt_publisher.py`.
2. **Node-RED dashboard** receives and displays this data in real time.
3. When new data arrives:
   - It's passed to `predict_days_to_clean.py` via Node-RED's `exec` node.
   - The script predicts days until next cleaning based on ML logic.
   - If the predicted days ≤ 5, an automatic **email alert** is sent.
4. The result is displayed on the dashboard in a widget: `Next Cleaning (days)`.

---

## 📦 Requirements

- **Python 3.9+**
- **Node-RED**
- **Mosquitto MQTT Broker**
- **Python Libraries:**
  - `scikit-learn`
  - `paho-mqtt`
  - `pandas`
  - `numpy`
  - `flask` (optional for expansion)

Install all dependencies:

```bash
pip install -r requirements.txt
```
---

## 📊 Node-RED Dashboard
**The UI contains:**

  - Line graphs for temperature, voltage, and dust level

  - A professional widget showing Next Cleaning (days)

  - A visual warning for urgent cleaning needs

  - Debug console for live message inspection

---

## 📬 Email Notification Setup
**Configure your Node-RED Email node with:**

  - SMTP server: smtp.gmail.com

  - Port: 465 or 587

  - Use secure connection (SSL/TLS)

  - Enter your Gmail credentials (preferably use App Password)

---

## 🤖 Why This Matters
Solar panels operate best when clean—but manual cleaning schedules often lead to over-maintenance or underperformance. This system introduces smart predictive cleaning using real-time data and ML, enabling:

  - Increased panel efficiency

  - Reduced cleaning cost and water usage

  - Improved operational transparency

---

## ✍️ Author
**Syed Ahmed Zulfiqar**
  - Final-Year Electronics Engineering Student
  - NED University of Engineering & Technology
  - [📫 LinkedIn Profile](https://www.linkedin.com/in/syed-ahmed-zulfiqar/)
