'''CRUD en fastApi'''
from fastapi import FastAPI
from typing import List
from uuid import UUID
from fastapi import HTTPException
from uuid import uuid4
from models import genero, Rol, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Marco",
        apellidos="Luna",
        genero=genero.Masculino,
        Rol=[Rol.Admin],
        correo="marco.luna@example.com",
        contrasena="password123"
    ),
    Usuario(
        id=uuid4(),
        nombre="lia",
        apellidos="Romero",
        genero=genero.Femenino,
        Rol=[Rol.User],
        correo="lia.romero@example.com",
        contrasena="password123"
    ),
    Usuario(
        id=uuid4(),
        nombre="Ricardo",
        apellidos="Morales",
        genero=genero.Masculino,
        Rol=[Rol.User],
        correo="ricardo.morales@example.com",
        contrasena="password123"
    ),
    Usuario(
        id=uuid4(),
        nombre="Jazmin",
        apellidos="Garrido",
        genero=genero.Femenino,
        Rol=[Rol.User],
        correo="jazmin.garrido@example.com",
        contrasena="password123"
    )
]

@app.get("/")
async def root():
    return {"Saludo": "Hola"}

@app.get("/api/users")
async def get_users():
    return db

@app.post("/api/users")
async def create_user(user: Usuario):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "Usuario eliminado"}
    raise HTTPException(
        status_code=404, detail=f"error al eliminar, {id} no encontrado"
    )
