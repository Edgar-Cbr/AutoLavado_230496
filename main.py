"""
API de usuarios usando FastAPI.

Permite crear, consultar, actualizar y eliminar usuarios en memoria.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from model import Usuario, Genero, Role


app = FastAPI(title="API Usuarios", version="1.0.0")

DB: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Raul",
        apellidos="Rufino Pazos",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Edwin",
        apellidos="Rosales Garcia",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Angel",
        apellidos="Artiaga Carrillo",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN],
    ),
]


@app.get("/")
async def root() -> dict:
    """
    Endpoint raíz de la API.

    Returns:
        dict: Mensaje de bienvenida.
    """
    return {"message": "Hola mundo"}


@app.get("/api/v1/usuarios", response_model=List[Usuario])
async def get_users() -> List[Usuario]:
    """
    Obtener todos los usuarios.

    Returns:
        List[Usuario]: Lista de usuarios.
    """
    return DB


@app.get("/api/v1/usuarios/{user_id}", response_model=Usuario)
async def get_user(user_id: UUID) -> Usuario:
    """
    Obtener un usuario por su ID.

    Args:
        user_id (UUID): Identificador del usuario.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        Usuario: Usuario encontrado.
    """
    for user in DB:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.put("/api/v1/usuarios/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, usuario: Usuario) -> Usuario:
    """
    Actualizar un usuario existente.

    Args:
        user_id (UUID): Identificador del usuario.
        usuario (Usuario): Datos actualizados.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        Usuario: Usuario actualizado.
    """
    for index, user in enumerate(DB):
        if user.id == user_id:
            usuario.id = user_id
            DB[index] = usuario
            return usuario

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/usuarios/{user_id}")
async def delete_user(user_id: UUID) -> dict:
    """
    Eliminar un usuario por su ID.

    Args:
        user_id (UUID): Identificador del usuario.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        dict: Mensaje de confirmación.
    """
    for index, user in enumerate(DB):
        if user.id == user_id:
            DB.pop(index)
            return {"mensaje": "Usuario eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")
