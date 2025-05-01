import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running!"}

def test_predict_valid_input():
    test_data = {
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
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "Anxiety Prediction" in response.json()
    assert "Stress Prediction" in response.json()
    assert "Depression Prediction" in response.json()

def test_predict_invalid_age():
    test_data = {
        "Age": 150.0,  # Invalid age
        "Gender": 1,
        # ... other fields ...
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 422

def test_predict_invalid_cgpa():
    test_data = {
        "Age": 20.0,
        "CGPA": 5.0,  # Invalid CGPA
        "Gender": 1,
        # ... other fields ...
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 422

def test_predict_missing_field():
    test_data = {
        "Age": 20.0,
        "Gender": 1,
        # Missing required fields
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 422 