import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
data = pd.read_csv("data/raw/metrics.csv")

# Set figure size
plt.figure(figsize=(14, 10))

# Plot CPU and Memory with Anomalies
plt.subplot(2, 1, 1)
plt.plot(data["timestamp"], data["cpu_percent"], label="CPU", color="blue", linewidth=2)
plt.scatter(data[data["label"] == 1]["timestamp"], 
            data[data["label"] == 1]["cpu_percent"], 
            color="red", s=50, label="Anomaly", zorder=5)
plt.xticks(rotation=45)
plt.xlabel("Timestamp")
plt.ylabel("CPU Percentage")
plt.title("CPU Usage with Anomalies")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))

# Plot GPU Usage
plt.subplot(2, 1, 2)
plt.plot(data["timestamp"], data["gpu_usage"], label="GPU", color="green", linewidth=2)
plt.xticks(rotation=45)
plt.xlabel("Timestamp")
plt.ylabel("GPU Usage")
plt.title("GPU Usage")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))

# Adjust layout and save figure
plt.tight_layout()
plt.savefig("results/metrics_visualization.png")
plt.show()
