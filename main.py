from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from database.db import Base, SessionLocal, engine
from models.contact import Contact
from repositories.contact import ContactRepository
from schemas.contact import ContactRequest, ContactResponse
from services.get_coins import GetCoins

Base.metadata.create_all(bind=engine)


description = """
Value Coin API helps you do awesome stuff. 🚀
"""


app = FastAPI(
    title="value-coins",
    description=description,
    version="0.0.1",
    contact={
        "name": "Tiago Lemos",
        "url": "https://www.linkedin.com/in/tiago-lemos-6b5213172/",
        "email": "lemosbeats@gmail.com",
    },
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def heath_check():
    return {"status": "OK"}


@app.get("/api/coins/{coin}", tags=["scrapy"])
def get_coin(coin: str):
    """Coins available: Dollar, Euro"""
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
    tags=["contacts"],
)
def create(request: ContactRequest, db: Session = Depends(get_db)):
    contact = ContactRepository.save(db, Contact(**request.dict()))
    return ContactResponse.from_orm(contact)


@app.get(
    "/api/contacts",
    response_model=list[ContactResponse],
    tags=["contacts"],
)
def find_all(db: Session = Depends(get_db)):
    cursos = ContactRepository.find_all(db)
    return [ContactResponse.from_orm(curso) for curso in cursos]


@app.get(
    "/api/contacts/{id}",
    response_model=ContactResponse,
    tags=["contacts"],
)
def find_by_id(id: int, db: Session = Depends(get_db)):
    contact = ContactRepository.find_by_id(db, id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return ContactResponse.from_orm(contact)


@app.put("/api/cursos/{id}", response_model=ContactResponse, tags=["contacts"])
def update(id: int, request: ContactRequest, db: Session = Depends(get_db)):
    if not ContactRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado",
        )
    curso = ContactRepository.save(db, Contact(id=id, **request.dict()))
    return ContactResponse.from_orm(curso)


@app.delete(
    "/api/contacts/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["contacts"],
)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ContactRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    ContactRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
