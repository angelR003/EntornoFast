from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class genero (str, Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class Rol(str, Enum):
    Admin = "Admin"
    User = "User"

class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre: str
    apellidos: str
    genero: genero
    Rol: List[Rol]

class UpdateUsuario(BaseModel):
    nombre: Optional[str]
    apellidos: Optional[str]
    genero: Optional[str]
    roles: Optional[List[Rol]]