import os

import databases
import sqlalchemy.orm
from fastapi_users.db import SQLAlchemyUserDatabase

from ..schemas.user import UserDB
from . import UserTable

DATABASE_URL = os.getenv("DATABASE_URL")
engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = databases.Database(DATABASE_URL)

users_table = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users_table)
