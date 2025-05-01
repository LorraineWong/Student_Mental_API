import joblib
import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)

# Load models and scaler once
try:
    model_anx = joblib.load("models/catboost_anxiety_model.pkl")
    model_str = joblib.load("models/catboost_stress_model.pkl")
    model_dep = joblib.load("models/catboost_depression_model.pkl")
    scaler = joblib.load("models/standard_scaler.pkl")
except Exception as e:
    logger.error(f"Error loading models: {str(e)}")
    raise RuntimeError("Failed to load required model files")

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
    """
    Make predictions using the loaded models
    
    Args:
        input_dict (dict): Input data dictionary
        
    Returns:
        dict: Predictions for anxiety, stress, and depression
        
    Raises:
        ValueError: If input data is invalid
        RuntimeError: If prediction fails
    """
    try:
        # Check required fields
        missing_fields = [field for field in feature_mapping.keys() if field not in input_dict]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        # Rename features
        try:
            renamed_dict = {feature_mapping[k]: v for k, v in input_dict.items()}
        except KeyError as e:
            raise ValueError(f"Invalid feature name: {str(e)}. Please check the input data format.")
        
        # Convert to DataFrame with correct column order
        try:
            columns = scaler.feature_names_in_
            input_df = pd.DataFrame([renamed_dict])[columns]
        except Exception as e:
            raise ValueError(f"Error creating input DataFrame: {str(e)}")
        
        # Scale
        try:
            input_scaled = scaler.transform(input_df)
        except Exception as e:
            raise ValueError(f"Error scaling input data: {str(e)}")
        
        # Predict
        try:
            pred_anx = int(model_anx.predict(input_scaled)[0])
            pred_str = int(model_str.predict(input_scaled)[0])
            pred_dep = int(model_dep.predict(input_scaled)[0])
        except Exception as e:
            raise RuntimeError(f"Error during model prediction: {str(e)}")
        
        # Validate prediction ranges
        if not (0 <= pred_anx <= 3):
            raise RuntimeError(f"Invalid anxiety prediction: {pred_anx}")
        if not (0 <= pred_str <= 2):
            raise RuntimeError(f"Invalid stress prediction: {pred_str}")
        if not (0 <= pred_dep <= 5):
            raise RuntimeError(f"Invalid depression prediction: {pred_dep}")
        
        return {
            "Anxiety Prediction": pred_anx,
            "Stress Prediction": pred_str,
            "Depression Prediction": pred_dep
        }
        
    except ValueError as e:
        logger.error(f"Validation error in prediction: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in prediction: {str(e)}")
        raise RuntimeError(f"Prediction failed: {str(e)}")
