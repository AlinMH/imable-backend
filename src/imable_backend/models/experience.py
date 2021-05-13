from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base_model import Base


class Experience(Base):
    __tablename__ = "experience"
    id = Column(Integer, primary_key=True)
    user_id = Column(GUID, ForeignKey("usertable.id"))
    position = Column(String(length=100), nullable=False)
    employer = Column(String(length=100), nullable=False)
    city = Column(String(length=100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    description = Column(String(length=1000), nullable=True)

    user = relationship("UserTable", back_populates="experience")
