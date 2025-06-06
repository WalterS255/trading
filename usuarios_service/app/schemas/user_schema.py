from pydantic import BaseModel, EmailStr, constr
from enum import Enum

class UserRole(str, Enum):
    cliente = "cliente"
    comisionista = "comisionista"
    auditor = "auditor"
    admin = "admin"

class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: constr(min_length=6)
    role: UserRole

class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True