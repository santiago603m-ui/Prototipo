from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    url: str

class CategoriaCrear(CategoriaBase):
    pass

class CategoriaActualizar(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    url: Optional[str] = None

class CategoriaResponse(CategoriaBase):
    idcategoria: int
