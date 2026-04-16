"""
config.py - Configuración centralizada de la aplicación.
Usa Pydantic Settings para leer las variables de entorno desde el archivo .env.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Configuracion(BaseSettings):
    """
    Clase de configuración que carga automáticamente las variables
    de entorno necesarias para conectarse a Supabase.
    """

    # Variables de entorno requeridas para Supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str

    # Metadatos de la API
    nombreProyecto: str = "Prototipo Backend FastAPI"
    descripcionProyecto: str = "Backend con FastAPI y Supabase - Arquitectura Limpia"
    versionApi: str = "1.0.0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def obtenerConfiguracion() -> Configuracion:
    """
    Retorna una instancia cacheada de la configuración.
    Se usa lru_cache para evitar leer el .env en cada solicitud.
    """
    return Configuracion()
