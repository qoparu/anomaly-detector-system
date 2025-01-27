# scripts/clean_csv.py
import pandas as pd

# Read raw data with error handling
try:
    data = pd.read_csv("data/raw/metrics.csv", error_bad_lines=False)
except pd.errors.ParserError:
    # If corrupted, reload with low-level parsing
    with open("data/raw/metrics.csv", "r") as f:
        lines = f.readlines()
    # Remove lines with incorrect column count
    header = lines[0].strip().split(",")
    valid_lines = [line for line in lines if len(line.split(",")) == len(header)]
    with open("data/raw/metrics_clean.csv", "w") as f:
        f.writelines(valid_lines)
    data = pd.read_csv("data/raw/metrics_clean.csv")

data.to_csv("data/raw/metrics_clean.csv", index=False)
print("CSV file cleaned successfully!")