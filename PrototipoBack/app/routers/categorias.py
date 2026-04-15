from fastapi import APIRouter, HTTPException, status
from typing import List

from app.database import supabaseClient
from app.schemas.categoria import CategoriaCrear, CategoriaActualizar, CategoriaResponse

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crearCategoria(categoriaData: CategoriaCrear):
    try:
        resultadoSupabase = supabaseClient.table("categorias").insert(categoriaData.model_dump()).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=400, detail="No se pudo crear la categoría")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[CategoriaResponse])
def obtenerCategorias():
    try:
        resultadoSupabase = supabaseClient.table("categorias").select("*").execute()
        return resultadoSupabase.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{idcategoria}", response_model=CategoriaResponse)
def obtenerCategoriaPorId(idcategoria: int):
    try:
        resultadoSupabase = supabaseClient.table("categorias").select("*").eq("idcategoria", idcategoria).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{idcategoria}", response_model=CategoriaResponse)
def actualizarCategoria(idcategoria: int, categoriaData: CategoriaActualizar):
    datosActualizar = categoriaData.model_dump(exclude_unset=True)
    if not datosActualizar:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")
    
    try:
        resultadoSupabase = supabaseClient.table("categorias").update(datosActualizar).eq("idcategoria", idcategoria).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Categoría no encontrada o no actualizada")
        return resultadoSupabase.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{idcategoria}", status_code=status.HTTP_204_NO_CONTENT)
def eliminarCategoria(idcategoria: int):
    try:
        resultadoSupabase = supabaseClient.table("categorias").delete().eq("idcategoria", idcategoria).execute()
        if not resultadoSupabase.data:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
