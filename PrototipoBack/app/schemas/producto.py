from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
import os

URL_BASE_ESTATICA = "http://localhost:8000/estatico"

class ProductoBase(BaseModel):
    nombre: str
    slug: str
    descripcion: Optional[str] = None
    precio: float = Field(..., ge=0, description="El precio no puede ser negativo")
    stock: int = Field(..., ge=0, description="El stock no puede ser negativo")
    esdestacado: bool = False
    idcategoria: int

class ProductoCrear(ProductoBase):
    pass

class ProductoActualizar(BaseModel):
    nombre: Optional[str] = None
    slug: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)
    imagenurl: Optional[str] = None 
    esdestacado: Optional[bool] = None
    idcategoria: Optional[int] = None

class ProductoLeer(ProductoBase):
    idproducto: int
    imagenurl: Optional[str] = None 

    model_config = ConfigDict(from_attributes=True)

    @field_validator("imagenurl")
    @classmethod
    def construir_url_completa(cls, v: str) -> str:
        if v and not v.startswith("http"):
            return f"{URL_BASE_ESTATICA}/{v}"
        return v