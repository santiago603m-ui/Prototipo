"""
producto.py - Modelo de negocio para la entidad Producto.
Contiene los nombres de la tabla y columnas como constantes
para evitar errores por cadenas de texto sueltas (magic strings).
"""


class ProductoModelo:
    """
    Representación de la tabla 'productos' en la base de datos.
    Actúa como fuente única de verdad para los nombres de tabla y columnas.
    """

    NOMBRE_TABLA = "productos"

    # Nombres de columnas
    ID_PRODUCTO = "idproducto"
    NOMBRE = "nombre"
    SLUG = "slug"
    DESCRIPCION = "descripcion"
    PRECIO = "precio"
    STOCK = "stock"
    IMAGEN_URL = "imagenurl"
    ES_DESTACADO = "esdestacado"
    ID_CATEGORIA = "idcategoria"
