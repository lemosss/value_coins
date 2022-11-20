from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "postgresql://postgres:postgres@127.0.0.1:5432/coins",
    echo=True
)
Base = declarative_base()
SessionLocal=sessionmaker(bind=engine)