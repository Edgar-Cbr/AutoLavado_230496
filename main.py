from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from model import Usuario, Genero, Role
from fastapi import HTTPException

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Raul",
        apellidos="Rufino Pazos",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN]
    ),
        Usuario(
        id=uuid4(),
        nombre="Edwin",
        apellidos="Rosales Garcia",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN]
    ),
        Usuario(
        id=uuid4(),
        nombre="Angel",
        apellidos="Artiaga Carrillo",
        genero=Genero.MASCULINO,
        roles=[Role.ADMIN]
    ),
]

@app.get("/")
async def root():
    return {"message":"Hola mundo"}

@app.get("/api/v1/usuarios")
async def get_users():
    return db
@app.get("/api/v1/usuarios/{user_id}")
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
@app.put("/api/v1/usuarios/{user_id}")
async def update_user(user_id: UUID, usuario: Usuario):
    for index, user in enumerate(db):
        if user.id == user_id:
            usuario.id = user_id  # mantenemos el ID original
            db[index] = usuario
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
@app.delete("/api/v1/usuarios/{user_id}")
async def delete_user(user_id: UUID):
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")