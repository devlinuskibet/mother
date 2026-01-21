import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Define dummy data (mimicking Maternal Health Dataset)
# Features: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate
X = np.array([
    [25, 120, 80, 7.0, 98.0, 70],  # Low Risk example
    [35, 140, 90, 8.5, 99.0, 80],  # Mid Risk example
    [40, 160, 100, 15.0, 101.0, 90] # High Risk example
])
y = np.array(["low risk", "mid risk", "high risk"])

# 2. Train a simple model
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# 3. Save the model to the ml_models folder
output_dir = "ml_models"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

model_path = os.path.join(output_dir, "maternal_risk_model.pkl")
joblib.dump(clf, model_path)

print(f"Dummy model saved to: {model_path}")
print("You can now proceed to build the inference service.")
