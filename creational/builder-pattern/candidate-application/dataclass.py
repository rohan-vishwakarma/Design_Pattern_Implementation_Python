from dataclasses import dataclass
from pydantic import BaseModel, Field, model_validator

class PersonalInformation(BaseModel):
    first_name :str = Field(..., description="first name is required", min_length=2)
    middle_name :str
    last_name :str = Field(..., description="last name is required", min_length=2)
    phone :str = Field(..., description="phone is required", min_length=10, max_length=10)
    location :str

class WorkExperience(BaseModel):
    employer :str = Field(..., description="employer is required")
    from_date :str = Field(..., description="from date is required")
    to_date :str
    role :str = Field(..., description="role is required")
    is_current: bool

    @model_validator(mode="after")
    def validate_to_date(cls, model):
        if not model.is_current and not model.to_date:
            raise ValueError("to_date is required when is_current is false")

        if model.is_current and model.to_date:
            raise ValueError("to_date must be empty when is_current is true")

        return model

@dataclass
class Education:
    institute :str
    degree :str
    duration :int

@dataclass
class CandidateApplication:
    personal_information: PersonalInformation
    education: Education
    work_experience: WorkExperience


