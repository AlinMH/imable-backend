from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..schemas.language import LanguageLevel
from .base_model import Base


class Language(Base):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True)
    user_id = Column(GUID, ForeignKey("usertable.id"))

    language = Column(String(length=40), nullable=False)
    level = Column(Enum(LanguageLevel), nullable=False)
    user = relationship("UserTable", back_populates="language")
