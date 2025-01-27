# scripts/inject_anomalies.py
import multiprocessing
import time
import os
import numpy as np

ANOMALY_FLAG = "anomaly_active.flag"

def cpu_stress(duration=60):
    end_time = time.time() + duration
    while time.time() < end_time:
        _ = 1 + 1

def memory_leak(duration=60):
    data = []
    end_time = time.time() + duration
    while time.time() < end_time:
        data.append(np.zeros((1024, 1024)))  # 1MB block
        time.sleep(0.1)

def disk_stress(duration=60):
    end_time = time.time() + duration
    while time.time() < end_time:
        with open("stress_file", "wb") as f:
            f.write(os.urandom(1024 * 1024))  # 1MB random data
        os.remove("stress_file")

def simulate_anomalies(anomaly_type="cpu", duration=60):
    func_map = {
        "cpu": cpu_stress,
        "memory": memory_leak,
        "disk": disk_stress
    }
    
    with open(ANOMALY_FLAG, "w") as f:
        f.write("ACTIVE")
    
    print(f"🚀 Injecting {anomaly_type} stress for {duration}s...")
    processes = [multiprocessing.Process(target=func_map[anomaly_type], args=(duration,)) for _ in range(4)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    if os.path.exists(ANOMALY_FLAG):
        os.remove(ANOMALY_FLAG)

if __name__ == "__main__":
    simulate_anomalies(anomaly_type="cpu", duration=60)