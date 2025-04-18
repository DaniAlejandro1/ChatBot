from fastapi import APIRouter, Query
from src.service.clima import get_weather
from src.utils.response_format import ResponseFormat


router = APIRouter(prefix="/clima")

@router.get("/")
async def clima(ciudad: str = Query(...)):
    try:
        data = await get_weather(ciudad)
        return ResponseFormat.success(data)
    except Exception as e:
        return ResponseFormat.error("404", "No se encontró", {"detalle": "clima no disponible"})