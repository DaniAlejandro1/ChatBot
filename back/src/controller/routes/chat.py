from fastapi import APIRouter
from src.service.chat import chat

router = APIRouter()

@router.get("/chat")
async def hola(topico : str):
    frase = await chat(frase=topico)
    print("frase", frase)
    return  frase
