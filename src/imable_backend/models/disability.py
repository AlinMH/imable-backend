from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..schemas.disability import DisabilityLevel, DisabilityType
from .base_model import Base


class Disability(Base):
    __tablename__ = "disability"
    id = Column(Integer, primary_key=True)
    user_id = Column(GUID, ForeignKey("usertable.id"))

    type = Column(Enum(DisabilityType), nullable=False)
    level = Column(Enum(DisabilityLevel), nullable=False)
    user = relationship("UserTable", back_populates="disability")
