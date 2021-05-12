from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(models.BaseUserCreate):
    first_name: str
    last_name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
