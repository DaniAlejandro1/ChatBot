from fastapi import APIRouter
from src.service.chat import chat

router = APIRouter()

@router.get("/chat")
async def hola():
    return  chat(frase="dolar")

@router.post("/name/{name}")
async def saludo(name):
    return "Hola " + name