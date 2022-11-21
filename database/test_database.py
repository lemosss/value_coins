import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import Base

sys.path.append("...")

SQLALCHEMY_DATABASE_URL = "sqlite:///testdb.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()