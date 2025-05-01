# Model Files

This directory contains the trained machine learning models and scaler used by the API.

## Required Files

1. `catboost_anxiety_model.pkl` - CatBoost model for anxiety prediction
2. `catboost_stress_model.pkl` - CatBoost model for stress prediction
3. `catboost_depression_model.pkl` - CatBoost model for depression prediction
4. `standard_scaler.pkl` - StandardScaler for feature normalization

## Model Information

### Prediction Levels
- 0: No symptoms
- 1: Mild symptoms
- 2: Severe symptoms

### Feature Importance
The models use the following features:
- Age
- Gender
- University
- Department
- Academic Year
- CGPA
- Various psychological assessment scores (1-3 scale)

## Model Performance

The models were trained and validated on a dataset of student mental health assessments. Performance metrics are available in the model training documentation.

## Usage

These models are automatically loaded by the API when it starts. No manual intervention is required.

## Security Note

These model files contain sensitive information and should not be committed to version control. They should be distributed separately or stored in a secure model registry. 