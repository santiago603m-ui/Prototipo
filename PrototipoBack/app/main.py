"""
main.py - Punto de entrada principal de la aplicación.
Configura FastAPI, CORS y registra los routers de la API v1.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import obtenerConfiguracion
from app.api.v1.api import routerApiV1

# Obtener la configuración centralizada
configuracion = obtenerConfiguracion()

# Crear la instancia principal de FastAPI
app = FastAPI(
    title=configuracion.nombreProyecto,
    description=configuracion.descripcionProyecto,
    version=configuracion.versionApi
)

# Configuración de CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers de la API versión 1 con prefijo /api/v1
app.include_router(routerApiV1, prefix="/api/v1")


@app.get("/", tags=["Salud"])
async def verificarSalud():
    """
    Endpoint de verificación de salud del servidor.
    Retorna el estado actual de la aplicación.
    """
    return {
        "estado": "ok",
        "mensaje": "Backend funcionando correctamente (Arquitectura Limpia)"
    }
