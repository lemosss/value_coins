from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database.database import Base, SessionLocal, engine
from models.models import Contact
from repositories.repository import ContactRepository
from schemas.schemas import ContactRequest, ContactResponse
from services.get_coins import GetCoins

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post(
    "/api/contacts",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(request: ContactRequest, db: Session = Depends(get_db)):
    contact = ContactRepository.save(db, Contact(**request.dict()))
    return ContactResponse.from_orm(contact)


@app.get("/api/contacts", response_model=list[ContactResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = ContactRepository.find_all(db)
    return [ContactResponse.from_orm(curso) for curso in cursos]
