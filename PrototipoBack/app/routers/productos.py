from fastapi import APIRouter, HTTPException, status
from typing import List

from app.database import supabaseClient
from app.schemas.producto import ProductoCrear, ProductoActualizar, ProductoResponse

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crearProducto(productoData: ProductoCrear):
    try:
        resultadoSupabase = supabaseClient.table("productos").insert(productoData.model_dump()).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=400, detail="No se pudo crear el producto")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ProductoResponse])
def obtenerProductos():
    try:
        resultadoSupabase = supabaseClient.table("productos").select("*").execute()
        return resultadoSupabase.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{idproducto}", response_model=ProductoResponse)
def obtenerProductoPorId(idproducto: int):
    try:
        resultadoSupabase = supabaseClient.table("productos").select("*").eq("idproducto", idproducto).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{idproducto}", response_model=ProductoResponse)
def actualizarProducto(idproducto: int, productoData: ProductoActualizar):
    datosActualizar = productoData.model_dump(exclude_unset=True)
    if not datosActualizar:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")
        
    try:
        resultadoSupabase = supabaseClient.table("productos").update(datosActualizar).eq("idproducto", idproducto).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Producto no encontrado o no actualizado")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{idproducto}", status_code=status.HTTP_204_NO_CONTENT)
def eliminarProducto(idproducto: int):
    try:
        resultadoSupabase = supabaseClient.table("productos").delete().eq("idproducto", idproducto).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
