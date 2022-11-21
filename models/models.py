from sqlalchemy import Column, Integer, String

from database.database import Base


class Contact(Base):
    __tablename__ = "contacts"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)
    email: str = Column(String(255), nullable=False)
    tel: str = Column(String(13), nullable=False)
