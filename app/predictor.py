import joblib
import numpy as np
import pandas as pd

# Load models and scaler once
model_anx = joblib.load("models/catboost_anxiety_model.pkl")
model_str = joblib.load("models/catboost_stress_model.pkl")
model_dep = joblib.load("models/catboost_depression_model.pkl")
scaler = joblib.load("models/standard_scaler.pkl")

# Feature name mapping
feature_mapping = {
    'Age': 'Age',
    'Gender': 'Gender',
    'University': 'University',
    'Department': 'Department',
    'Academic_Year': 'Academic Year',
    'CGPA': 'Current CGPA',
    'Waiver_Scholarship': 'Waiver/Scholarship',
    'Nervous_Anxious': 'Nervous/Anxious',
    'Worrying': 'Worrying',
    'Trouble_Relaxing': 'Trouble Relaxing ',
    'Easily_Annoyed': 'Easily Annoyed',
    'Excessive_Worry': 'Excessive Worry ',
    'Restless': 'Restless',
    'Fearful': 'Fearful ',
    'Upset': 'Upset',
    'Lack_of_Control': 'Lack of Control',
    'Nervous_Stress': 'Nervous/Stress ',
    'Inadequate_Coping': 'Inadequate Coping',
    'Confident': 'Confident',
    'Things_Going_Well': 'Things Going Well',
    'Control_Irritations': 'Control Irritations',
    'Top_Performance': 'Top Performance',
    'Angered_by_Performance': 'Angered by Performance',
    'Overwhelmed': 'Overwhelmed',
    'Lack_of_Interest': 'Lack of Interest',
    'Feeling_Down': 'Feeling Down',
    'Sleep_Issues': 'Sleep Issues',
    'Fatigue': 'Fatigue',
    'Appetite_Issues': 'Appetite Issues',
    'Self_Doubt': 'Self-Doubt',
    'Concentration_Issues': 'Concentration Issues',
    'Movement_Issues': 'Movement Issues',
    'Suicidal_Thoughts': 'Suicidal Thoughts'
}

def predict_from_input(input_dict: dict) -> dict:
    try:
        # Rename features
        renamed_dict = {feature_mapping[k]: v for k, v in input_dict.items()}
        
        # Convert to DataFrame with correct column order
        columns = scaler.feature_names_in_
        input_df = pd.DataFrame([renamed_dict])[columns]
        
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
    except KeyError as e:
        raise ValueError(f"Invalid feature name: {str(e)}. Please check the input data format.")
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")
