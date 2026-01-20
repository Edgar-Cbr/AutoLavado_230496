#model.py

from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Genero (str, Enum):
    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"

class Role(str, Enum):
    ADMIN = "Admin"
    USER = "User"

class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role] = [Role.USER]