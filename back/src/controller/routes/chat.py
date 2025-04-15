from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def hola():
    return  "hello world"

@router.get("/name")
async def saludo():
    nombre = "hola"
    print(nombre)
    return "Hola Jorge"