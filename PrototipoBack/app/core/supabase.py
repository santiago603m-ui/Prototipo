"""
supabase.py - Inicialización del cliente de Supabase.
Exporta una instancia única del cliente lista para usar en los servicios.
"""

from supabase import create_client, Client
from app.core.config import obtenerConfiguracion

# Obtener la configuración desde las variables de entorno
configuracion = obtenerConfiguracion()

# Crear e inicializar el cliente de Supabase
clienteSupabase: Client = create_client(
    configuracion.SUPABASE_URL,
    configuracion.SUPABASE_KEY
)
