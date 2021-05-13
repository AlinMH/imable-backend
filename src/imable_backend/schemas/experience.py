from datetime import date

from pydantic import BaseModel, constr


class Experience(BaseModel):
    position: constr(max_length=100)
    employer: constr(max_length=100)
    city: constr(max_length=100)
    description: constr(max_length=1000)
    start_date: date
    end_date: date


class ExperienceDB(Experience):
    id: int = None
