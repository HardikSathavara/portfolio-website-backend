from pydantic import BaseModel, EmailStr

class UserQuery(BaseModel):
    query: str

class BotResponse(BaseModel):
    status: str
    message: str