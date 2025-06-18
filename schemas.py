from pydantic import BaseModel, EmailStr


class TestSchema(BaseModel):
    name: str
    email: EmailStr
    count: int
