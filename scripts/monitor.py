# scripts/monitor.py
import os
import psutil
import time
import csv
import GPUtil
from datetime import datetime

print("Starting monitor.py...")

def collect_metrics(interval=1, output_file="data/raw/metrics.csv"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    headers = [
        "timestamp", "cpu_percent", "cpu_temp", "memory_percent",
        "disk_usage", "network_activity", "process_count",
        "gpu_usage", "io_read", "io_write", "label"
    ]
    
    try:
        with open(output_file, "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(headers)
            
            print("Monitoring started. Press Ctrl+C to stop.")
            while True:
                # System metrics
                timestamp = datetime.now().isoformat()
                cpu = psutil.cpu_percent()
                memory = psutil.virtual_memory().percent
                disk = psutil.disk_usage("/").percent
                network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
                processes = len(psutil.pids())
                io_read = psutil.disk_io_counters().read_bytes
                io_write = psutil.disk_io_counters().write_bytes
                
                # GPU metrics
                try:
                    gpu = GPUtil.getGPUs()[0].load * 100  # First GPU usage
                except Exception:
                    gpu = 0.0
                
                # CPU temperature (Linux only)
                try:
                    temp = psutil.sensors_temperatures()["coretemp"][0].current
                except Exception:
                    temp = 0.0
                
                # Labeling
                label = 1 if os.path.exists("anomaly_active.flag") else 0
                
                writer.writerow([
                    timestamp, cpu, temp, memory, disk,
                    network, processes, gpu, io_read, io_write, label
                ])
                print(f"[{timestamp}] CPU: {cpu}% | GPU: {gpu}% | Label: {label}")
                time.sleep(interval)
                
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    collect_metrics()