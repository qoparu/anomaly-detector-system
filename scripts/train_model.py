# scripts/train_model.py
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import classification_report, roc_auc_score
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense

# Load data
data = pd.read_csv("data/raw/metrics_clean.csv")  # <-- Use cleaned CSV
features = data.drop(["timestamp", "label"], axis=1)
labels = data["label"]

# Algorithm Comparison
models = {
    "Isolation Forest": IsolationForest(n_estimators=150, contamination=0.1),
    "One-Class SVM": OneClassSVM(nu=0.1),
    "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, novelty=True)
}

best_score = 0
best_model = None

for name, model in models.items():
    print(f"\n=== Training {name} ===")
    
    if name == "Local Outlier Factor":
        preds = model.fit_predict(features)
    else:
        model.fit(features)
        preds = model.predict(features)
    
    preds = np.where(preds == -1, 1, 0)  # Convert to binary labels
    report = classification_report(labels, preds)
    roc_auc = roc_auc_score(labels, preds)
    
    print(report)
    print(f"ROC-AUC: {roc_auc:.2f}")
    
    if roc_auc > best_score:
        best_score = roc_auc
        best_model = model

# Save best model
joblib.dump(best_model, "models/best_model.pkl")
print(f"\n🔥 Best Model: {type(best_model).__name__} | ROC-AUC: {best_score:.2f}")

# Deep Autoencoder
print("\n=== Training Autoencoder ===")
autoencoder = Sequential([
    Dense(64, activation='relu', input_shape=(features.shape[1],)),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(features.shape[1], activation='linear')
])
autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(features, features, epochs=50, batch_size=32, validation_split=0.2)
autoencoder.save("models/autoencoder.h5")

# Autoencoder evaluation
reconstructions = autoencoder.predict(features)
mse = np.mean(np.square(features - reconstructions), axis=1)
threshold = np.quantile(mse, 0.95)
preds = (mse > threshold).astype(int)
print(classification_report(labels, preds))

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(features["cpu_percent"], features["memory_percent"], c=labels, cmap="coolwarm")
plt.xlabel("CPU Usage (%)")
plt.ylabel("Memory Usage (%)")
plt.savefig("results/feature_distribution.png")