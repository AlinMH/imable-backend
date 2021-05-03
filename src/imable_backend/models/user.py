from fastapi_users.db import SQLAlchemyBaseUserTable
from .base_model import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass
