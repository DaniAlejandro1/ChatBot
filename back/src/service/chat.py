import asyncio
from src.utils.modelo_ia import detectar_intencion
from src.service.clima import get_clima
from src.service.dolar import get_valor_dolar
from src.service.uf import get_valor_uf
from src.service.noticias import get_noticias_recientes
from ..utils.modelo_ia import parafrasear_texto

acciones = {
    "uf": get_valor_uf,
    "dolar": get_valor_dolar,
    "clima": lambda: get_clima(ciudad="Temuco"),
    "noticias": get_noticias_recientes,
    "desconocida": lambda: "Lo siento, no entiendo tu pregunta.",
}

async def chat(frase):
    intention = detectar_intencion(frase)
    funcion = acciones.get(intention, acciones["desconocida"])
    print(f"Intención detectada: {intention}")
    
    if intention == "desconocida":
        return funcion()
    
    resultado = await funcion()
    print(f"Resultado de la función: {resultado}")
    if intention != "noticias":
        return parafrasear_texto(frase, resultado)
    
    return resultado
    
