from fastapi import FastAPI
from app.schema import MentalHealthInput
from app.predictor import predict_from_input

app = FastAPI(title="Mental Health Prediction API")

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.post("/predict")
def predict(input_data: MentalHealthInput):
    return predict_from_input(input_data.dict())

