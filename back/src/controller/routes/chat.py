from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def hola():
    return  "hello world"

@router.post("/name/{name}")
async def saludo(name):
    return "Hola " + name