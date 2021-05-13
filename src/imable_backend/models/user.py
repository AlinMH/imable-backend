from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, Date, String
from sqlalchemy.orm import relationship

from .base_model import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    first_name = Column(String(length=40), nullable=True)
    last_name = Column(String(length=40), nullable=True)
    phone_number = Column(String(length=50), nullable=True)
    location = Column(String(length=50), nullable=True)
    birthdate = Column(Date, nullable=True)

    # Abilities
    creativity = Column(Boolean, nullable=True)
    analytic_thinking = Column(Boolean, nullable=True)
    communication = Column(Boolean, nullable=True)
    teamwork = Column(Boolean, nullable=True)
    adaptive = Column(Boolean, nullable=True)

    # Hobbies
    walking = Column(Boolean, nullable=True)
    painting = Column(Boolean, nullable=True)
    video_games = Column(Boolean, nullable=True)
    reading = Column(Boolean, nullable=True)
    movies = Column(Boolean, nullable=True)
    writing = Column(Boolean, nullable=True)
    singing = Column(Boolean, nullable=True)
    music = Column(Boolean, nullable=True)
    audio_books = Column(Boolean, nullable=True)

    experience = relationship("Experience", back_populates="user")
    education = relationship("Education", back_populates="user")
    language = relationship("Language", back_populates="user")
    disability = relationship("Disability", back_populates="user")
