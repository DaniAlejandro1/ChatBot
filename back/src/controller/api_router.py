from fastapi import APIRouter
from .routes import chat
from .routes import clima_router

api_router = APIRouter()

api_router.include_router(chat.router, prefix="", tags=["Chat"]
)

api_router.include_router(clima_router.router, prefix="", tags=["Clima"]
)