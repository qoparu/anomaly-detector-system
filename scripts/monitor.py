import os
import psutil
import time
import csv
from datetime import datetime

print("Starting monitor.py...")

def collect_metrics(interval=1, output_file="data/raw/metrics.csv"):
    # Create directory if missing
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    headers = ["timestamp", "cpu_percent", "memory_percent", "disk_usage", "network_activity"]
    
    try:
        with open(output_file, "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(headers)
            
            print("Monitoring started. Press Ctrl+C to stop.")
            while True:
                # Collect metrics
                timestamp = datetime.now().isoformat()
                cpu = psutil.cpu_percent()
                memory = psutil.virtual_memory().percent
                disk = psutil.disk_usage("/").percent
                network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
                
                # Write to CSV and print debug info
                writer.writerow([timestamp, cpu, memory, disk, network])
                print(f"[{timestamp}] CPU: {cpu}% | Memory: {memory}%")  # Debug print
                time.sleep(interval)
                
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    print("Monitor.py is running...")
    collect_metrics()