"""
categoria.py - Esquemas Pydantic para la entidad Categoría.
Separa los esquemas de creación (Request) de los de lectura (Response).
"""

from pydantic import BaseModel, ConfigDict
from typing import Optional


class CategoriaBase(BaseModel):
    """
    Esquema base de Categoría con los campos compartidos.
    Se usa como clase padre para Creación y Lectura.
    """

    nombre: str
    descripcion: Optional[str] = None
    url: str


class CategoriaCrear(CategoriaBase):
    """
    Esquema para la creación de una nueva categoría (Request).
    No incluye el campo idcategoria ya que es autogenerado por la BD.
    """

    pass


class CategoriaActualizar(BaseModel):
    """
    Esquema para la actualización parcial de una categoría (PATCH).
    Todos los campos son opcionales para soportar actualizaciones parciales.
    """

    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    url: Optional[str] = None


class CategoriaLeer(CategoriaBase):
    """
    Esquema de lectura de categoría (Response).
    Incluye el idcategoria generado por la base de datos.
    """

    idcategoria: int

    model_config = ConfigDict(from_attributes=True)
