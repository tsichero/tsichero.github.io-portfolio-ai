from pydantic import BaseModel, ConfigDict, EmailStr


class ContactCreate(BaseModel):
    name: str
    email: EmailStr


class ContactResponse(ContactCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
