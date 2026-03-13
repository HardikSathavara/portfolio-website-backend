from pydantic import BaseModel, EmailStr

class InquiryCreate(BaseModel):
    name: str
    email: EmailStr
    country: str
    mobile: str
    message: str

class InquiryResponse(BaseModel):
    status: str
    message: str