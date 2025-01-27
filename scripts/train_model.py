# scripts/train_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load and preprocess data
data = pd.read_csv("data/processed/training_data.csv")
X = data.drop("label", axis=1)  # Features: cpu_percent, memory_percent, etc.
y = data["label"]               # 0=normal, 1=anomaly

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Isolation Forest (unsupervised)
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(X_train)
y_pred = model.predict(X_test)
y_pred = [1 if x == -1 else 0 for x in y_pred]  # Convert to binary labels

# Evaluate
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/trained_model.pkl")