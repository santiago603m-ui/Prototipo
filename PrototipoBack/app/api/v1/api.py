"""
api.py - Agregador de routers para la versión 1 de la API.
Centraliza todos los enrutadores de endpoints en un solo router principal.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import categorias, productos

# Router principal que agrupa todos los endpoints de la v1
routerApiV1 = APIRouter()

# Incluir los enrutadores de cada entidad
routerApiV1.include_router(categorias.router)
routerApiV1.include_router(productos.router)
