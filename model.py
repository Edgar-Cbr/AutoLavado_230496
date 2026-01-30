"""
Modelos de datos para la API de usuarios.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """
    Enumeración de géneros disponibles.
    """

    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"


class Role(str, Enum):
    """
    Enumeración de roles de usuario.
    """

    ADMIN = "Admin"
    USER = "User"


class Usuario(BaseModel):
    """
    Modelo que representa un usuario del sistema.
    """

    id: Optional[UUID] = Field(default_factory=uuid4)
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role] = Field(default_factory=lambda: [Role.USER])
