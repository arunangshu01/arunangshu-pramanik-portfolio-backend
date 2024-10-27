from pydantic import BaseModel, EmailStr
from fastapi import Form


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

    @classmethod
    def as_form(cls,
                name: str = Form(...),
                email: EmailStr = Form(...),
                subject: str = Form(...),
                message: str = Form(...)):
        return cls(name=name, email=email, subject=subject, message=message)


class SendMessageSuccess(BaseModel):
    message: str
