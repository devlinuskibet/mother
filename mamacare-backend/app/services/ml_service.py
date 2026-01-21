import joblib
import numpy as np
import os
from datetime import datetime

class MLService:
    def __init__(self):
        self.model = None
        self.model_path = "ml_models/maternal_risk_model.pkl"
        self.load_model()

    def load_model(self):
        """Loads the model from disk if it exists."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print("✅ Model loaded successfully.")
        else:
            print(f"⚠️ Model file not found at {self.model_path}")
            self.model = None

    def predict(self, input_data: list):
        """
        Runs inference on the input data.
        Returns: Risk Label (str) and Probability (float).
        """
        if not self.model:
            return "Error: Model not loaded", 0.0

        # Convert list to 2D numpy array (1 row, N features)
        features = np.array(input_data).reshape(1, -1)
        
        # Get prediction (e.g., "high risk")
        prediction = self.model.predict(features)[0]
        
        # Get probability (confidence)
        # We take the max probability among the classes
        probability = np.max(self.model.predict_proba(features))

        return prediction, probability

# Create a single instance to be imported elsewhere
ml_service = MLService()