# scripts/detect_anomalies.py
import joblib
import psutil
import time
import GPUtil
import numpy as np
import os
from datetime import datetime

try:
    model = joblib.load("models/best_model.pkl")
except FileNotFoundError:
    print("ERROR: Model not found. Train the model first with 'python scripts/train_model.py'")
    exit(1)

def get_system_metrics():
    return [
        psutil.cpu_percent(),
        psutil.sensors_temperatures().get('coretemp', [[0.0]])[0].current,
        psutil.virtual_memory().percent,
        psutil.disk_usage("/").percent,
        psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv,
        len(psutil.pids()),
        GPUtil.getGPUs()[0].load * 100 if GPUtil.getGPUs() else 0.0,
        psutil.disk_io_counters().read_bytes,
        psutil.disk_io_counters().write_bytes
    ]

def detect_anomalies(interval=1, threshold=-0.5):
    while True:
        metrics = get_system_metrics()
        score = model.decision_function([metrics])[0] if hasattr(model, 'decision_function') else 0
        
        if score < threshold:
            timestamp = datetime.now().isoformat()
            alert_msg = f"[{timestamp}] ALERT: Anomaly detected (Score: {score:.2f})"
            print(alert_msg)
            with open("alerts.log", "a") as f:
                f.write(alert_msg + "\n")
        
        time.sleep(interval)

if __name__ == "__main__":
    detect_anomalies(threshold=-0.5)