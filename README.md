# Anomaly Detector System

## Overview
The Anomaly Detector System is designed to identify unusual patterns in data that do not conform to expected behavior. This system can be used in various domains such as fraud detection, network security, and fault detection.

## Features
- Real-time anomaly detection
- Support for multiple data sources
- Customizable detection algorithms
- Detailed reporting and visualization

## Installation
To install the Anomaly Detector System, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/anomaly-detector-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd anomaly-detector-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
The project exposes a command line interface through `main.py`. Use one of the
subcommands below depending on the action you want to perform:

```bash
# Train the model
python main.py train

# Collect system metrics
python main.py monitor

# Inject anomalies (e.g. CPU stress for 60s)
python main.py inject --type cpu --duration 60

# Run live anomaly detection
python main.py detect
```
