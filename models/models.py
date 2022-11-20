from database.database import Base
from sqlalchemy import Column, Integer, String


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    tel = Column(Integer)

    def __repr__(self):
        return f"<Contact name={self.name} Email={self.email} Tel={self.tel}>"
