from typing import List
from fastapi import FastAPI, HTTPException, status
from models.models import Contact
from schemas.schemas import ContactSchema
from services.get_coins import GetCoins
from database.database import SessionLocal


db = SessionLocal()

app = FastAPI()


@app.get("/")
def heath_check():
    return {"status": "OK"}


@app.get("/items/{coin}")
def get_coin(coin: str):
    if coin == "dollar":
        dollar = GetCoins.get_dollar()
        return {"dollar_value": dollar}
    if coin == "euro":
        euro = GetCoins.get_euro()
        return {"euro_value": euro}
    else:
        raise HTTPException(status_code=400, detail="Invalid Coin")


@app.get("/contacts", response_model=List[ContactSchema], status_code=200)
def get_contacts():
    contacts = db.query(Contact).all()
    return contacts


@app.post(
    "/create/contact",
    response_model=ContactSchema,
    status_code=status.HTTP_201_CREATED
)
def create_contracts(contact: ContactSchema):
    new_contact = Contact(
        name=contact.name,
        email=contact.email,
        tel=contact.tel,
    )
    db.add(new_contact)
    db.commit()
    return new_contact
