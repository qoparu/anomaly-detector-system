# scripts/detect_anomalies.py
import joblib
import psutil
import time
from monitor import collect_metrics  # Reuse monitoring logic

model = joblib.load("models/trained_model.pkl")

def detect_anomalies(interval=1):
    while True:
        # Collect current metrics
        metrics = [psutil.cpu_percent(), psutil.virtual_memory().percent, ...]
        prediction = model.predict([metrics])
        
        if prediction == -1:
            print(f"ALERT: Anomaly detected at {time.ctime()}")
        time.sleep(interval)

if __name__ == "__main__":
    detect_anomalies()