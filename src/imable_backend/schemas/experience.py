from datetime import date
from typing import Optional

from pydantic import BaseModel, constr


class Experience(BaseModel):
    position: constr(max_length=100)
    employer: constr(max_length=100)
    city: constr(max_length=100)
    start_date: date
    end_date: date
    description: Optional[constr(max_length=1000)]


class ExperienceDB(Experience):
    id: int = None
