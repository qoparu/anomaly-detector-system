import argparse
import subprocess
import sys
import os

# Allow importing modules from the scripts directory
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import monitor
import inject_anomalies
import detect_anomalies


def train_command(args):
    """Train the anomaly detection model using the training script."""
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "train_model.py")], check=True)


def monitor_command(args):
    """Start system metrics collection."""
    monitor.collect_metrics(interval=args.interval, output_file=args.output)


def inject_command(args):
    """Inject artificial anomalies into the system."""
    inject_anomalies.simulate_anomalies(anomaly_type=args.type, duration=args.duration)


def detect_command(args):
    """Run the real-time anomaly detector."""
    detect_anomalies.detect_anomalies(interval=args.interval, threshold=args.threshold)


def build_parser():
    parser = argparse.ArgumentParser(description="Anomaly Detector System CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # train
    train_parser = subparsers.add_parser("train", help="Train the anomaly detection model")
    train_parser.set_defaults(func=train_command)

    # monitor
    monitor_parser = subparsers.add_parser("monitor", help="Monitor and record system metrics")
    monitor_parser.add_argument("--interval", type=int, default=1, help="Sampling interval in seconds")
    monitor_parser.add_argument("--output", default="data/raw/metrics.csv", help="CSV file to store metrics")
    monitor_parser.set_defaults(func=monitor_command)

    # inject
    inject_parser = subparsers.add_parser("inject", help="Inject system anomalies for testing")
    inject_parser.add_argument("--type", choices=["cpu", "memory", "disk"], default="cpu", help="Anomaly type")
    inject_parser.add_argument("--duration", type=int, default=60, help="Duration of anomaly in seconds")
    inject_parser.set_defaults(func=inject_command)

    # detect
    detect_parser = subparsers.add_parser("detect", help="Run real-time anomaly detection")
    detect_parser.add_argument("--interval", type=int, default=1, help="Detection interval in seconds")
    detect_parser.add_argument("--threshold", type=float, default=-0.5, help="Anomaly score threshold")
    detect_parser.set_defaults(func=detect_command)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
