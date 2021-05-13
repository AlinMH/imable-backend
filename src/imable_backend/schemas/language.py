from enum import Enum

from pydantic import BaseModel, constr


class LanguageLevel(Enum):
    BEGINNER = "BEGINNER"
    MEDIUM = "MEDIUM"
    ADVANCED = "ADVANCED"
    NATIVE = "NATIVE"


class Language(BaseModel):
    level: LanguageLevel
    language: constr(max_length=40)

    class Config:
        use_enum_values = True


class LanguageDB(Language):
    id: int = None
