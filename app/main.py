from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schema import MentalHealthInput
from app.predictor import predict_from_input
import traceback
import logging
import json
from typing import Dict, Any
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/api.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Student Mental Health Assessment API",
    description="API for predicting student mental health conditions using machine learning models",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware to log all requests"""
    start_time = datetime.now()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url}")
    
    try:
        # Get request body for POST requests
        if request.method == "POST":
            body = await request.body()
            try:
                body_json = json.loads(body)
                logger.info(f"Request body: {body_json}")
            except json.JSONDecodeError:
                logger.warning("Invalid JSON in request body")
        
        # Process request
        response = await call_next(request)
        
        # Log response
        process_time = (datetime.now() - start_time).total_seconds()
        logger.info(f"Response: {response.status_code} (took {process_time:.2f}s)")
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "API is running!"}

@app.post("/predict")
async def predict(input_data: MentalHealthInput) -> Dict[str, Any]:
    """
    Predict mental health conditions based on student data
    
    Args:
        input_data (MentalHealthInput): Student data including demographic and psychological assessment scores
        
    Returns:
        Dict[str, Any]: Predictions for anxiety, stress, and depression levels
        
    Raises:
        HTTPException: If there are validation errors or prediction errors
    """
    try:
        # Convert input data to dict
        input_dict = input_data.model_dump()
        
        # Log the prediction request
        logger.info(f"Received prediction request for student with Age: {input_dict['Age']}, Gender: {input_dict['Gender']}")
        
        # Make prediction
        result = predict_from_input(input_dict)
        
        # Log the prediction result
        logger.info(f"Prediction result: {result}")
        
        return result
        
    except ValueError as ve:
        # Handle validation errors
        error_msg = str(ve)
        logger.error(f"Validation error: {error_msg}")
        raise HTTPException(
            status_code=422,
            detail={
                "error": "Validation Error",
                "message": error_msg,
                "type": "validation_error"
            }
        )
        
    except Exception as e:
        # Handle unexpected errors
        error_msg = str(e)
        stack_trace = traceback.format_exc()
        logger.error(f"Unexpected error: {error_msg}\n{stack_trace}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal Server Error",
                "message": "An unexpected error occurred during prediction",
                "type": "server_error"
            }
        )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle request validation errors"""
    error_messages = []
    for error in exc.errors():
        error_messages.append({
            "field": " -> ".join(str(x) for x in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    logger.error(f"Request validation error: {error_messages}")
    return JSONResponse(
        status_code=422,
        content={
            "error": "Request Validation Error",
            "details": error_messages,
            "type": "validation_error"
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Custom exception handler for HTTP exceptions"""
    logger.error(f"HTTP error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Custom exception handler for unexpected exceptions"""
    logger.error(f"Unexpected error: {str(exc)}\n{traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred",
            "type": "server_error"
        }
    ) 