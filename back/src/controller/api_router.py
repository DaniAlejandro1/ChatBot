from fastapi import APIRouter
from .routes import chat
from .routes import clima_router
from .routes import uf_router
from .routes import dolar_router
from .routes import noticias_router

api_router = APIRouter()

api_router.include_router(chat.router, prefix="", tags=["Chat"])

api_router.include_router(clima_router.router, prefix="", tags=["Clima"])

api_router.include_router(uf_router.router, prefix="", tags=["UF"])

api_router.include_router(dolar_router.router, prefix="", tags=["Dólar"])

api_router.include_router(noticias_router.router, prefix="", tags=["Noticias"])