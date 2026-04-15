from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Asegúrate de importar los módulos desde app.routers
from app.routers import categorias, productos

app = FastAPI(
    title="Prototipo Backend FastAPI",
    description="Backend con FastAPI y Supabase Modularizado",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los enrutadores (routers)
app.include_router(categorias.router)
app.include_router(productos.router)

@app.get("/", tags=["Health"])
def healthCheck():
    return {"status": "ok", "message": "Backend funcionando correctamente (Arquitectura Modular)"}
