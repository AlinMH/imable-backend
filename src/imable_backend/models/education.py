from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..schemas.education import EduType
from .base_model import Base


class Education(Base):
    __tablename__ = "education"
    id = Column(Integer, primary_key=True)
    user_id = Column(GUID, ForeignKey("usertable.id"))
    edu_type = Column(Enum(EduType), nullable=False)
    name = Column(String(length=100), nullable=False)
    city = Column(String(length=100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    user = relationship("UserTable", back_populates="education")
