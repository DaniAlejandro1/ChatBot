from fastapi import APIRouter, Query
from src.service.clima import get_clima
from src.utils.response_format import ResponseFormat


router = APIRouter()

@router.get("/chat/topico/clima")
async def clima():
    ciudad = "Temuco"
    try:
        data = await get_clima(ciudad)
        return ResponseFormat.success_clima(data)
    except Exception:
        return ResponseFormat.error_personalizado()