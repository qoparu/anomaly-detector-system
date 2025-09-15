# Anomaly Detector System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-blue?logo=eclipse-mosquitto)](https://mosquitto.org/)
[![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

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
<div align="center"> <h3>✨ Crafted with ❤️ by <a href="https://github.com/qoparu">Aru</a> ✨</h3> <p>For the <b>Data Collection and Machine Learning</b> exam</p> </div>
