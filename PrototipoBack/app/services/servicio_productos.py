"""
servicio_productos.py - Capa de servicio para la entidad Producto.
Contiene la lógica CRUD que consume el cliente de Supabase.
Separa la lógica de negocio de los endpoints (controladores).
"""

from app.core.supabase import clienteSupabase
from app.models.producto import ProductoModelo
from app.schemas.producto import ProductoCrear, ProductoActualizar


async def listarProductos() -> list:
    """
    Obtiene todos los productos desde la base de datos.
    Retorna una lista de diccionarios con los datos de cada producto.
    """
    resultado = clienteSupabase.table(
        ProductoModelo.NOMBRE_TABLA
    ).select("*").execute()

    return resultado.data


async def obtenerProductoPorId(idProducto: int) -> dict | None:
    """
    Busca un producto específico por su ID.
    Retorna el diccionario del producto o None si no existe.
    """
    resultado = clienteSupabase.table(
        ProductoModelo.NOMBRE_TABLA
    ).select("*").eq(
        ProductoModelo.ID_PRODUCTO, idProducto
    ).execute()

    if not resultado.data:
        return None

    return resultado.data[0]


async def crearProducto(datosProducto: ProductoCrear) -> dict:
    """
    Crea un nuevo producto en la base de datos.
    Recibe un esquema de creación y retorna los datos del producto creado.
    """
    resultado = clienteSupabase.table(
        ProductoModelo.NOMBRE_TABLA
    ).insert(
        datosProducto.model_dump()
    ).execute()

    return resultado.data[0]


async def actualizarProducto(idProducto: int, datosProducto: ProductoActualizar) -> dict | None:
    datosActualizar = datosProducto.model_dump(exclude_unset=True)

    if not datosActualizar:
        return None

    resultado = clienteSupabase.table(
        ProductoModelo.NOMBRE_TABLA
    ).update(datosActualizar).eq(
        ProductoModelo.ID_PRODUCTO, idProducto
    ).execute()

    if not resultado.data:
        return None

    return resultado.data[0]


async def eliminarProducto(idProducto: int) -> bool:
    """
    Elimina un producto de la base de datos por su ID.
    Retorna True si se eliminó correctamente, False si no se encontró.
    """
    resultado = clienteSupabase.table(
        ProductoModelo.NOMBRE_TABLA
    ).delete().eq(
        ProductoModelo.ID_PRODUCTO, idProducto
    ).execute()

    return bool(resultado.data)
