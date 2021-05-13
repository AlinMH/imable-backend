from enum import Enum

from pydantic import BaseModel, constr


class DisabilityLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    ADVANCED = "ADVANCED"
    HIGH = "HIGH"


class DisabilityType(Enum):
    VISUAL = "VISUAL"
    HEARING = "HEARING"
    SPEECH = "SPEECH"
    LOCOMOTOR = "LOCOMOTOR"
    NEURAL = "NEURAL"


class Disability(BaseModel):
    level: DisabilityLevel
    type: DisabilityType

    class Config:
        use_enum_values = True


class DisabilityDB(Disability):
    id: int = None
