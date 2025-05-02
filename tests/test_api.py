import json
import requests
import pytest
from typing import Dict, Any

BASE_URL = "http://localhost:8006"

def load_test_data() -> Dict[str, Any]:
    with open("tests/test_data.json", "r") as f:
        return json.load(f)

def test_root_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running!"}

def test_valid_prediction():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test_data["valid_data"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    result = response.json()
    assert "Anxiety Prediction" in result
    assert "Stress Prediction" in result
    assert "Depression Prediction" in result

def test_invalid_age():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test_data["invalid_age"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert any("Age" in detail["loc"] for detail in error["detail"])
    assert any("100" in detail["msg"] for detail in error["detail"])

def test_invalid_cgpa():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test_data["invalid_cgpa"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert any("CGPA" in detail["loc"] for detail in error["detail"])
    assert any("4" in detail["msg"] for detail in error["detail"])

def test_invalid_scale():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test_data["invalid_scale"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert any("Gender" in detail["loc"] for detail in error["detail"])
    assert any("between 1 and 3" in detail["msg"] for detail in error["detail"])

def test_missing_fields():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        json=test_data["missing_fields"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert len(error["detail"]) > 0
    assert any("Field required" in detail["msg"] for detail in error["detail"])

def test_invalid_json():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        data=test_data["invalid_json"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert any("JSON decode error" in detail["msg"] for detail in error["detail"])

def test_empty_json():
    test_data = load_test_data()
    response = requests.post(
        f"{BASE_URL}/predict",
        data=test_data["empty_json"],
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    error = response.json()
    assert "detail" in error
    assert len(error["detail"]) > 0
    assert any("Field required" in detail["msg"] for detail in error["detail"])

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 