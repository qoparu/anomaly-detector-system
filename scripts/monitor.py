import psutil
import time
import csv
from datetime import datetime

print("Starting monitor.py...")

def collect_metrics(interval=1, output_file="metrics.csv"):
    headers = ["timestamp", "cpu_percent", "memory_percent", "disk_usage", "network_activity"]
    
    with open(output_file, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:  # Write headers only once
            writer.writerow(headers)
        
        while True:
            timestamp = datetime.now().isoformat()
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent
            network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            
            writer.writerow([timestamp, cpu, memory, disk, network])
            time.sleep(interval)

if __name__ == "__main__":
    collect_metrics()
    
    print("Monitor.py is running...")
