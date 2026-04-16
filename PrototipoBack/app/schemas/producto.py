"""
producto.py - Esquemas Pydantic para la entidad Producto.
Separa los esquemas de creación (Request) de los de lectura (Response).
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class ProductoBase(BaseModel):
    """
    Esquema base de Producto con los campos compartidos y validaciones.
    Se usa como clase padre para Creación y Lectura.
    """

    nombre: str
    slug: str
    descripcion: Optional[str] = None
    precio: float = Field(..., ge=0, description="El precio no puede ser negativo")
    stock: int = Field(..., ge=0, description="El stock no puede ser negativo")
    imagenurl: Optional[str] = None
    esdestacado: bool = False
    idcategoria: int


class ProductoCrear(ProductoBase):
    """
    Esquema para la creación de un nuevo producto (Request).
    No incluye el campo idproducto ya que es autogenerado por la BD.
    """

    pass


class ProductoActualizar(BaseModel):
    """
    Esquema para la actualización parcial de un producto (PATCH).
    Todos los campos son opcionales para soportar actualizaciones parciales.
    """

    nombre: Optional[str] = None
    slug: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)
    imagenurl: Optional[str] = None
    esdestacado: Optional[bool] = None
    idcategoria: Optional[int] = None


class ProductoLeer(ProductoBase):
    """
    Esquema de lectura de producto (Response).
    Incluye el idproducto generado por la base de datos.
    """

    idproducto: int

    model_config = ConfigDict(from_attributes=True)
