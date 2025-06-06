from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    CLIENTE = "cliente"
    COMISIONISTA = "comisionista"
    AUDITOR = "auditor"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SqlEnum(UserRole), default=UserRole.CLIENTE)