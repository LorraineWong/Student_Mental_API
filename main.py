from fastapi import FastAPI, HTTPException
from app.schema import MentalHealthInput
from app.predictor import predict_from_input
import traceback

app = FastAPI(title="Mental Health Prediction API")

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.post("/predict")
def predict(input_data: MentalHealthInput):
    try:
        # 验证输入数据
        input_dict = input_data.dict()
        
        # 检查所有必需字段是否存在
        required_fields = [
            "Age", "Gender", "University", "Department", "Academic_Year",
            "CGPA", "Waiver_Scholarship", "Nervous_Anxious", "Worrying",
            "Trouble_Relaxing", "Easily_Annoyed", "Excessive_Worry",
            "Restless", "Fearful", "Upset", "Lack_of_Control",
            "Nervous_Stress", "Inadequate_Coping", "Confident",
            "Things_Going_Well", "Control_Irritations", "Top_Performance",
            "Angered_by_Performance", "Overwhelmed", "Lack_of_Interest",
            "Feeling_Down", "Sleep_Issues", "Fatigue", "Appetite_Issues",
            "Self_Doubt", "Concentration_Issues", "Movement_Issues",
            "Suicidal_Thoughts"
        ]
        
        missing_fields = [field for field in required_fields if field not in input_dict]
        if missing_fields:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required fields: {', '.join(missing_fields)}"
            )
            
        # 验证数值范围
        if not (0 <= input_dict["Age"] <= 100):
            raise HTTPException(
                status_code=400,
                detail="Age must be between 0 and 100"
            )
            
        if not (0 <= input_dict["CGPA"] <= 4.0):
            raise HTTPException(
                status_code=400,
                detail="CGPA must be between 0 and 4.0"
            )
            
        # 验证其他字段的值范围（1-3）
        for field in required_fields:
            if field not in ["Age", "CGPA"] and not (1 <= input_dict[field] <= 3):
                raise HTTPException(
                    status_code=400,
                    detail=f"{field} must be between 1 and 3"
                )
        
        # 进行预测
        result = predict_from_input(input_dict)
        return result
        
    except HTTPException as he:
        raise he
    except Exception as e:
        # 记录详细错误信息
        error_detail = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        raise HTTPException(
            status_code=500,
            detail=error_detail
        )

