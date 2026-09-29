from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from .database import Base, SessionLocal, engine
from .models import Contact
from .schemas import ContactCreate, ContactResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Contacts API",
    version="1.0.0",
    description="CRUD API demonstrando FastAPI, validação e persistência.",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/contacts", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    if db.query(Contact).filter(Contact.email == payload.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")

    contact = Contact(name=payload.name, email=payload.email)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@app.get("/contacts", response_model=list[ContactResponse])
def list_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).order_by(Contact.id).all()


@app.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@app.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, payload: ContactCreate, db: Session = Depends(get_db)):
    contact = db.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    duplicate = (
        db.query(Contact)
        .filter(Contact.email == payload.email, Contact.id != contact_id)
        .first()
    )
    if duplicate:
        raise HTTPException(status_code=409, detail="Email already registered")

    contact.name = payload.name
    contact.email = payload.email
    db.commit()
    db.refresh(contact)
    return contact


@app.delete("/contacts/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    db.delete(contact)
    db.commit()
