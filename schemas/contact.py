from pydantic import BaseModel


class ContactBase(BaseModel):
    name: str
    email: str
    tel: str


class ContactRequest(ContactBase):
    ...


class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
