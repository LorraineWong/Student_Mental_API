# Model Files

This directory contains the machine learning models and related files used for mental health prediction.

## Files Description

1. `catboost_anxiety_model.pkl`
   - CatBoost model for anxiety level prediction
   - Trained on student mental health dataset
   - Output: Anxiety level (0-3)

2. `catboost_stress_model.pkl`
   - CatBoost model for stress level prediction
   - Trained on student mental health dataset
   - Output: Stress level (0-3)

3. `catboost_depression_model.pkl`
   - CatBoost model for depression level prediction
   - Trained on student mental health dataset
   - Output: Depression level (0-3)

4. `standard_scaler.pkl`
   - StandardScaler for feature normalization
   - Used to preprocess input features before prediction

## Model Information

### Training Data
- Dataset: Student Mental Health Survey
- Features: 33 input features including demographic and psychological assessment scores
- Target Variables: Anxiety, Stress, and Depression levels

### Model Performance
- Model Type: CatBoost Classifier
- Evaluation Metric: Accuracy and F1-score
- Cross-validation: 5-fold

### Prediction Levels

#### Anxiety Levels
- 0: Mild Anxiety
- 1: Minimal Anxiety
- 2: Moderate Anxiety
- 3: Severe Anxiety

#### Stress Levels
- 0: High Perceived Stress
- 1: Low Stress
- 2: Moderate Stress

#### Depression Levels
- 0: Mild Depression
- 1: Minimal Depression
- 2: Moderate Depression
- 3: Moderately Severe Depression
- 4: No Depression
- 5: Severe Depression

## Usage

These models are automatically loaded and used by the API's prediction endpoint. No manual interaction is required.

## Requirements

- scikit-learn
- catboost
- numpy
- pandas

## Note

Do not modify these model files directly. If you need to update the models, please retrain them using the training scripts and replace the files accordingly. 