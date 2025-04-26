from fastapi import APIRouter
from src.service.noticias import get_noticias_recientes
from src.utils.response_format import ResponseFormat

router = APIRouter()

@router.get("/chat/topico/noticias")
async def noticias():
    try:
        title = await get_noticias_recientes()
        return ResponseFormat.success_noticias({
            "title": title
        })
    except Exception:
        return ResponseFormat.error_personalizado()