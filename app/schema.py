from pydantic import BaseModel, Field, validator
from typing import Optional

class MentalHealthInput(BaseModel):
    # Special fields, need specific range validation
    Age: float = Field(ge=0, le=100)
    CGPA: float = Field(ge=0, le=4.0)
    
    # Basic information fields
    Gender: int
    University: int
    Department: int
    Academic_Year: int
    
    # Mental health assessment fields
    Waiver_Scholarship: int
    Nervous_Anxious: int
    Worrying: int
    Trouble_Relaxing: int
    Easily_Annoyed: int
    Excessive_Worry: int
    Restless: int
    Fearful: int
    Upset: int
    Lack_of_Control: int
    Nervous_Stress: int
    Inadequate_Coping: int
    Confident: int
    Things_Going_Well: int
    Control_Irritations: int
    Top_Performance: int
    Angered_by_Performance: int
    Overwhelmed: int
    Lack_of_Interest: int
    Feeling_Down: int
    Sleep_Issues: int
    Fatigue: int
    Appetite_Issues: int
    Self_Doubt: int
    Concentration_Issues: int
    Movement_Issues: int
    Suicidal_Thoughts: int

    @validator('Gender', 'University', 'Department', 'Academic_Year', 
              'Waiver_Scholarship', 'Nervous_Anxious', 'Worrying',
              'Trouble_Relaxing', 'Easily_Annoyed', 'Excessive_Worry',
              'Restless', 'Fearful', 'Upset', 'Lack_of_Control',
              'Nervous_Stress', 'Inadequate_Coping', 'Confident',
              'Things_Going_Well', 'Control_Irritations', 'Top_Performance',
              'Angered_by_Performance', 'Overwhelmed', 'Lack_of_Interest',
              'Feeling_Down', 'Sleep_Issues', 'Fatigue', 'Appetite_Issues',
              'Self_Doubt', 'Concentration_Issues', 'Movement_Issues',
              'Suicidal_Thoughts')
    def validate_scale(cls, v):
        if not 1 <= v <= 3:
            raise ValueError('Value must be between 1 and 3')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
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
        }
    }
