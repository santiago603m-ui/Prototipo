from pydantic import BaseModel, Field
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    slug: str
    descripcion: Optional[str] = None
    precio: float = Field(..., ge=0, description="El precio no puede ser negativo")
    stock: int = Field(..., ge=0, description="El stock no puede ser negativo")
    imagenurl: Optional[str] = None
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

class ProductoResponse(ProductoBase):
    idproducto: int
