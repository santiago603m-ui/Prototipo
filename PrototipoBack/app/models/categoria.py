"""
categoria.py - Modelo de negocio para la entidad Categoría.
Contiene los nombres de la tabla y columnas como constantes
para evitar errores por cadenas de texto sueltas (magic strings).
"""


class CategoriaModelo:
    """
    Representación de la tabla 'categorias' en la base de datos.
    Actúa como fuente única de verdad para los nombres de tabla y columnas.
    """

    NOMBRE_TABLA = "categorias"

    # Nombres de columnas
    ID_CATEGORIA = "idcategoria"
    NOMBRE = "nombre"
    DESCRIPCION = "descripcion"
    URL = "url"
