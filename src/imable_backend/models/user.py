from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String

from .base_model import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    first_name = Column(String(length=40), nullable=False)
    last_name = Column(String(length=40), nullable=False)
