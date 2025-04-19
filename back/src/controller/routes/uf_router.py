from fastapi import APIRouter
from src.service.uf import get_valor_uf
from src.utils.response_format import ResponseFormat

router = APIRouter()

@router.get("/chat/topico/uf")
async def obtener_valor_uf():
    try:
        mensaje = await get_valor_uf()
        return ResponseFormat.success_uf(mensaje)
    except Exception:
        return ResponseFormat.error_personalizado()
    