from fastapi import APIRouter
from src.service.dolar import get_valor_dolar
from src.utils.response_format import ResponseFormat

router = APIRouter()

@router.get("/chat/topico/dolar")
async def dolar():
    try:
        mensaje = await get_valor_dolar()
        return ResponseFormat.success_dolar({mensaje})
    except Exception:
        return ResponseFormat.error_personalizado()