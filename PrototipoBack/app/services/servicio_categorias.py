"""
servicio_categorias.py - Capa de servicio para la entidad Categoría.
Contiene la lógica CRUD que consume el cliente de Supabase.
Separa la lógica de negocio de los endpoints (controladores).
"""

from app.core.supabase import clienteSupabase
from app.models.categoria import CategoriaModelo
from app.schemas.categoria import CategoriaCrear, CategoriaActualizar


async def listarCategorias() -> list:
    """
    Obtiene todas las categorías desde la base de datos.
    Retorna una lista de diccionarios con los datos de cada categoría.
    """
    resultado = clienteSupabase.table(
        CategoriaModelo.NOMBRE_TABLA
    ).select("*").execute()

    return resultado.data


async def obtenerCategoriaPorId(idCategoria: int) -> dict | None:
    """
    Busca una categoría específica por su ID.
    Retorna el diccionario de la categoría o None si no existe.
    """
    resultado = clienteSupabase.table(
        CategoriaModelo.NOMBRE_TABLA
    ).select("*").eq(
        CategoriaModelo.ID_CATEGORIA, idCategoria
    ).execute()

    if not resultado.data:
        return None

    return resultado.data[0]


async def crearCategoria(datosCategoria: CategoriaCrear) -> dict:
    """
    Crea una nueva categoría en la base de datos.
    Recibe un esquema de creación y retorna los datos de la categoría creada.
    """
    resultado = clienteSupabase.table(
        CategoriaModelo.NOMBRE_TABLA
    ).insert(
        datosCategoria.model_dump()
    ).execute()

    return resultado.data[0]


async def actualizarCategoria(idCategoria: int, datosCategoria: CategoriaActualizar) -> dict | None:
    """
    Actualiza parcialmente una categoría existente.
    Solo modifica los campos que fueron enviados en la solicitud.
    Retorna los datos actualizados o None si la categoría no existe.
    """
    datosActualizar = datosCategoria.model_dump(exclude_unset=True)

    if not datosActualizar:
        return None

    resultado = clienteSupabase.table(
        CategoriaModelo.NOMBRE_TABLA
    ).update(datosActualizar).eq(
        CategoriaModelo.ID_CATEGORIA, idCategoria
    ).execute()

    if not resultado.data:
        return None

    return resultado.data[0]


async def eliminarCategoria(idCategoria: int) -> bool:
    """
    Elimina una categoría de la base de datos por su ID.
    Retorna True si se eliminó correctamente, False si no se encontró.
    """
    resultado = clienteSupabase.table(
        CategoriaModelo.NOMBRE_TABLA
    ).delete().eq(
        CategoriaModelo.ID_CATEGORIA, idCategoria
    ).execute()

    return bool(resultado.data)
