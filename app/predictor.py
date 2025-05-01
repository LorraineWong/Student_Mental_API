import joblib
import numpy as np
import pandas as pd

# Load models and scaler once
model_anx = joblib.load("models/catboost_anxiety_model.pkl")
model_str = joblib.load("models/catboost_stress_model.pkl")
model_dep = joblib.load("models/catboost_depression_model.pkl")
scaler = joblib.load("models/standard_scaler.pkl")

def predict_from_input(input_dict: dict) -> dict:
    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])
    # Scale
    input_scaled = scaler.transform(input_df)
    # Predict
    pred_anx = int(model_anx.predict(input_scaled)[0])
    pred_str = int(model_str.predict(input_scaled)[0])
    pred_dep = int(model_dep.predict(input_scaled)[0])
    return {
        "Anxiety Prediction": pred_anx,
        "Stress Prediction": pred_str,
        "Depression Prediction": pred_dep
    }
