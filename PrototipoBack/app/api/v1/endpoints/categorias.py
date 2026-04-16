"""
categorias.py - Endpoints (rutas) para la entidad Categoría.
Usa APIRouter para definir las rutas y delega la lógica al servicio.
Maneja errores con HTTPException en español.
"""

from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.categoria import CategoriaCrear, CategoriaActualizar, CategoriaLeer
from app.services import servicio_categorias as servicioCategorias

# Definición del enrutador para categorías
router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("/", response_model=List[CategoriaLeer], summary="Listar todas las categorías")
async def listarCategorias():
    """
    Obtiene el listado completo de categorías registradas.
    """
    try:
        categorias = await servicioCategorias.listarCategorias()
        return categorias
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener las categorías: {str(error)}"
        )


@router.get("/{idCategoria}", response_model=CategoriaLeer, summary="Obtener categoría por ID")
async def obtenerCategoriaPorId(idCategoria: int):
    """
    Obtiene una categoría específica por su identificador único.
    """
    try:
        categoria = await servicioCategorias.obtenerCategoriaPorId(idCategoria)

        if categoria is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"La categoría con ID {idCategoria} no fue encontrada"
            )

        return categoria
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar la categoría: {str(error)}"
        )


@router.post("/", response_model=CategoriaLeer, status_code=status.HTTP_201_CREATED, summary="Crear nueva categoría")
async def crearCategoria(datosCategoria: CategoriaCrear):
    """
    Crea una nueva categoría en el sistema.
    """
    try:
        nuevaCategoria = await servicioCategorias.crearCategoria(datosCategoria)
        return nuevaCategoria
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear la categoría: {str(error)}"
        )


@router.patch("/{idCategoria}", response_model=CategoriaLeer, summary="Actualizar categoría parcialmente")
async def actualizarCategoria(idCategoria: int, datosCategoria: CategoriaActualizar):
    """
    Actualiza parcialmente una categoría existente.
    Solo se modifican los campos enviados en la solicitud.
    """
    try:
        categoriaActualizada = await servicioCategorias.actualizarCategoria(idCategoria, datosCategoria)

        if categoriaActualizada is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"La categoría con ID {idCategoria} no fue encontrada o no hay datos para actualizar"
            )

        return categoriaActualizada
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar la categoría: {str(error)}"
        )


@router.delete("/{idCategoria}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar categoría")
async def eliminarCategoria(idCategoria: int):
    """
    Elimina una categoría del sistema por su ID.
    """
    try:
        eliminada = await servicioCategorias.eliminarCategoria(idCategoria)

        if not eliminada:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"La categoría con ID {idCategoria} no fue encontrada"
            )

        return None
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar la categoría: {str(error)}"
        )
