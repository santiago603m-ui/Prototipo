"""
productos.py - Endpoints (rutas) para la entidad Producto.
Usa APIRouter para definir las rutas y delega la lógica al servicio.
Maneja errores con HTTPException en español.
"""

from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.producto import ProductoCrear, ProductoActualizar, ProductoLeer
from app.services import servicio_productos as servicioProductos

# Definición del enrutador para productos
router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=List[ProductoLeer], summary="Listar todos los productos")
async def listarProductos():
    """
    Obtiene el listado completo de productos registrados.
    """
    try:
        productos = await servicioProductos.listarProductos()
        return productos
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener los productos: {str(error)}"
        )


@router.get("/{idProducto}", response_model=ProductoLeer, summary="Obtener producto por ID")
async def obtenerProductoPorId(idProducto: int):
    """
    Obtiene un producto específico por su identificador único.
    """
    try:
        producto = await servicioProductos.obtenerProductoPorId(idProducto)

        if producto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El producto con ID {idProducto} no fue encontrado"
            )

        return producto
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar el producto: {str(error)}"
        )


@router.post("/", response_model=ProductoLeer, status_code=status.HTTP_201_CREATED, summary="Crear nuevo producto")
async def crearProducto(datosProducto: ProductoCrear):
    """
    Crea un nuevo producto en el sistema.
    """
    try:
        nuevoProducto = await servicioProductos.crearProducto(datosProducto)
        return nuevoProducto
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear el producto: {str(error)}"
        )


@router.patch("/{idProducto}", response_model=ProductoLeer, summary="Actualizar producto parcialmente")
async def actualizarProducto(idProducto: int, datosProducto: ProductoActualizar):
    """
    Actualiza parcialmente un producto existente.
    Solo se modifican los campos enviados en la solicitud.
    """
    try:
        productoActualizado = await servicioProductos.actualizarProducto(idProducto, datosProducto)

        if productoActualizado is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El producto con ID {idProducto} no fue encontrado o no hay datos para actualizar"
            )

        return productoActualizado
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el producto: {str(error)}"
        )


@router.delete("/{idProducto}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar producto")
async def eliminarProducto(idProducto: int):
    """
    Elimina un producto del sistema por su ID.
    """
    try:
        eliminado = await servicioProductos.eliminarProducto(idProducto)

        if not eliminado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El producto con ID {idProducto} no fue encontrado"
            )

        return None
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar el producto: {str(error)}"
        )
