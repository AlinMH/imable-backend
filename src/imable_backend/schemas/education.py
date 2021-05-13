from datetime import date
from enum import Enum

from pydantic import BaseModel, constr


class EduType(Enum):
    MIDDLE_SCHOOL = "MIDDLE_SCHOOL"
    HIGH_SCHOOL = "HIGH_SCHOOL"
    UNIVERSITY = "UNIVERSITY"
    MASTER = "MASTER"
    PHD = "PHD"


class Education(BaseModel):
    edu_type: EduType
    name: constr(max_length=100)
    city: constr(max_length=100)
    start_date: date
    end_date: date

    class Config:
        use_enum_values = True


class EducationDB(Education):
    id: int = None
