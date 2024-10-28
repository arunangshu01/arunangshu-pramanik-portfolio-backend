from pydantic import BaseModel, EmailStr
from fastapi import Form


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

    @classmethod
    def as_form(cls,
                name: str = Form(...),
                email: EmailStr = Form(...),
                message: str = Form(...)):
        return cls(name=name, email=email, message=message)


class SendMessageSuccess(BaseModel):
    message: str
