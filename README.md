# Student Mental Health Assessment API

A FastAPI-based REST API for predicting student mental health conditions using machine learning models.

## Features

- Predicts anxiety, stress, and depression levels
- Input validation and error handling
- Scalable and production-ready architecture
- Comprehensive API documentation
- Easy to deploy and maintain

## Tech Stack

- Python 3.12+
- FastAPI
- Pydantic
- CatBoost
- scikit-learn
- uvicorn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Student_Mental_API.git
cd Student_Mental_API
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
uvicorn main:app --port 8000
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### 1. Health Check
- **GET** `/`
- Returns API status
- Response: `{"message": "API is running!"}`

### 2. Mental Health Prediction
- **POST** `/predict`
- Predicts anxiety, stress, and depression levels
- Request Body:
```json
{
    "Age": 20.0,
    "Gender": 1,
    "University": 1,
    "Department": 1,
    "Academic_Year": 2,
    "CGPA": 3.5,
    "Waiver_Scholarship": 1,
    "Nervous_Anxious": 2,
    "Worrying": 2,
    "Trouble_Relaxing": 1,
    "Easily_Annoyed": 1,
    "Excessive_Worry": 2,
    "Restless": 1,
    "Fearful": 1,
    "Upset": 1,
    "Lack_of_Control": 1,
    "Nervous_Stress": 2,
    "Inadequate_Coping": 1,
    "Confident": 3,
    "Things_Going_Well": 3,
    "Control_Irritations": 3,
    "Top_Performance": 3,
    "Angered_by_Performance": 1,
    "Overwhelmed": 1,
    "Lack_of_Interest": 1,
    "Feeling_Down": 1,
    "Sleep_Issues": 1,
    "Fatigue": 1,
    "Appetite_Issues": 1,
    "Self_Doubt": 1,
    "Concentration_Issues": 1,
    "Movement_Issues": 1,
    "Suicidal_Thoughts": 1
}
```
- Response:
```json
{
    "Anxiety Prediction": 2,
    "Stress Prediction": 2,
    "Depression Prediction": 0
}
```

## Input Validation

- Age: 0-100 (float)
- CGPA: 0-4.0 (float)
- All other fields: 1-3 (integer)
  - 1: Low
  - 2: Medium
  - 3: High

## Model Information

The API uses three CatBoost models for prediction:
1. Anxiety Model
2. Stress Model
3. Depression Model

Each model outputs a prediction level (0-2):
- 0: No symptoms
- 1: Mild symptoms
- 2: Severe symptoms

## Error Handling

The API includes comprehensive error handling for:
- Invalid input data
- Missing required fields
- Out-of-range values
- Model prediction errors

## Development

### Project Structure
```
Student_Mental_API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── predictor.py
│   └── schema.py
├── models/
│   ├── catboost_anxiety_model.pkl
│   ├── catboost_stress_model.pkl
│   ├── catboost_depression_model.pkl
│   └── standard_scaler.pkl
├── tests/
│   └── test_api.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Running Tests
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue in the GitHub repository.
