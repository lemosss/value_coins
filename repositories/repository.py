from sqlalchemy.orm import Session

from models.models import Contact


class ContactRepository:
    @staticmethod
    def find_all(db: Session) -> list[Contact]:
        return db.query(Contact).all()

    @staticmethod
    def save(db: Session, contact: Contact) -> Contact:
        if contact.id:
            db.merge(contact)
        else:
            db.add(contact)
        db.commit()
        return contact

    @staticmethod
    def find_by_id(db: Session, id: int) -> Contact:
        return db.query(Contact).filter(Contact.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Contact).filter(Contact.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        contact = db.query(Contact).filter(Contact.id == id).first()
        if contact is not None:
            db.delete(contact)
            db.commit()
