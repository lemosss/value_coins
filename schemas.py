from pydantic import BaseModel


class ContactSchema(BaseModel):
    id: int
    name: str
    email: str
    tel: int

    class Config:
        orm_mode = True


class MessageSchema(BaseModel):
    id: int
    message: str
    
    class Config:
        orm_mode = True
