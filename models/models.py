from sqlalchemy import Column, Integer, String

from database.database import Base


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    tel = Column(Integer)

    def __repr__(self):
        return f"Contact Name={self.name} Email={self.email} Tel={self.tel}"
