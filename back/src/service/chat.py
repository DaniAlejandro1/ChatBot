from src.utils.modelo_ia import detectar_intencion
from src.service.clima import obtener_clima
from src.service.dolar import obtener_dolar
from src.service.uf import obtener_uf
from src.service.noticias import obtener_noticias



acciones = {
    "uf": obtener_uf,
    "dolar": obtener_dolar,
    "clima": obtener_clima,
    "noticias": obtener_noticias,
    "desconocida": "Lo siento, no entiendo tu pregunta.",
}

def chat(frase):
    intention = detectar_intencion(frase)
    respuesta = acciones[intention](frase)
    
    
    return respuesta