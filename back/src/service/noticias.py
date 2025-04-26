import httpx
import os
import random
from src.utils.response_format import ResponseFormat



API_KEY = os.getenv("NOTICIAS_API_KEY")
URL = f"https://newsapi.org/v2/top-headlines/sources?language=es&apiKey={API_KEY}"

async def get_noticias_recientes():
   

    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        response.raise_for_status()
        data = response.json()
        if data["status"] == "ok" and data["sources"]:
            articulo = random.choice(data["sources"])
            
            return str(articulo["description"])
                #"nombre": articulo["name"],
                #"url": articulo["url"],
            
        else:
            return f"error", "No se encontraron noticias",str(response.json())
