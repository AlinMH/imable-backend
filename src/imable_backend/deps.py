from typing import Generator

import sqlalchemy.orm
from .database import session


def db_session() -> Generator[sqlalchemy.orm.Session, None, None]:
    session_ = None
    try:
        session_ = session.SessionLocal()
        yield session_
    finally:
        session_.close()
