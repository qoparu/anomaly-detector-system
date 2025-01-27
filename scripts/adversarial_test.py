# scripts/adversarial_test.py
from art.estimators.classification import SklearnClassifier
from art.attacks.evasion import FastGradientMethod
import joblib
import pandas as pd
import numpy as np

# Load model and data
model = joblib.load("models/best_model.pkl")
data = pd.read_csv("data/raw/metrics.csv")
X = data.drop(["timestamp", "label"], axis=1).values
y = data["label"].values

# Create ART classifier
classifier = SklearnClassifier(model=model)
attack = FastGradientMethod(classifier, eps=0.1)
X_adv = attack.generate(X)

# Evaluate adversarial samples
adv_preds = model.predict(X_adv)
adv_accuracy = np.mean(adv_preds == y)
print(f"Accuracy under attack: {adv_accuracy:.2%}")

# Save adversarial examples
adv_df = data.copy()
adv_df.iloc[:, 1:-1] = X_adv
adv_df.to_csv("data/adversarial_samples.csv", index=False)