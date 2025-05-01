# Student Mental Health Assessment API

A machine learning-based API for predicting student mental health conditions based on personal information and psychological assessment responses.

## Features

- Modern RESTful API built with FastAPI
- Machine learning models for mental health prediction
- Comprehensive input validation and error handling
- Detailed API documentation and test cases
- Cross-Origin Resource Sharing (CORS) support
- Logging functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Student_Mental_API.git
cd Student_Mental_API
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
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

2. API Endpoints:
   - Health Check: `GET /`
   - Prediction: `POST /predict`

### Prediction Endpoint Parameters

Request body (JSON format) should include the following fields:

```json
{
    "Age": 20.0,                    
    "Gender": 1,                    
    "University": 1,                
    "Department": 1,                
    "Academic_Year": 2,             
    "CGPA": 3.5,                    // CGPA (0-4.0)
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

### Prediction Results

Returns JSON format with three prediction values:

```json
{
    "Anxiety Prediction": 2,     // Anxiety Level (0-3)
    "Stress Prediction": 2,      // Stress Level (0-2)
    "Depression Prediction": 1    // Depression Level (0-5)
}
```

Prediction Level Explanation:

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

## Error Handling

API returns the following HTTP status codes:

- 200: Request Successful
- 422: Input Validation Error
  - Missing Required Fields
  - Field Values Out of Range
  - JSON Format Error
- 500: Internal Server Error

Error Response Format:
```json
{
    "detail": [
        {
            "loc": ["body", "field_name"],
            "msg": "error_message",
            "type": "error_type"
        }
    ]
}
```

## Testing

1. Install test dependencies:
```bash
pip install pytest requests
```

2. Run tests:
```bash
python -m pytest tests/test_api.py -v
```

Test cases include:
- Basic Functionality Tests
- Input Validation Tests
- Error Handling Tests
- JSON Format Tests

## Logging

API logs the following information:
- Request details (method, URL, request body)
- Response status code and processing time
- Error and exception information

Log file location: `logs/api.log`

## Development

- Framework: FastAPI
- Python Version: 3.12+
- Dependency Management: pip
- Testing Framework: pytest

## Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)
