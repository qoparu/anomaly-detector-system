# scripts/visualize.py
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/raw/metrics.csv")
plt.figure(figsize=(12, 8))

# CPU and Memory with Anomalies
plt.subplot(2, 1, 1)
plt.plot(data["timestamp"], data["cpu_percent"], label="CPU")
plt.scatter(data[data["label"]==1]["timestamp"], 
            data[data["label"]==1]["cpu_percent"], 
            color="red", label="Anomaly")
plt.xticks(rotation=45)
plt.legend()

# GPU Usage
plt.subplot(2, 1, 2)
plt.plot(data["timestamp"], data["gpu_usage"], label="GPU", color="green")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig("results/metrics_visualization.png")