from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship

from .base_model import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    first_name = Column(String(length=40), nullable=True)
    last_name = Column(String(length=40), nullable=True)
    phone_number = Column(String(length=50), nullable=True)
    location = Column(String(length=50), nullable=True)
    birthdate = Column(Date, nullable=True)

    experience = relationship("Experience", back_populates="user")
    education = relationship("Education", back_populates="user")
