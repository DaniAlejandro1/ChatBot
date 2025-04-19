import httpx
from datetime import date
import os
from dotenv import load_dotenv
from src.utils.response_format import ResponseFormat

load_dotenv()

API_KEY = os.getenv("CMF_API_KEY")
BASE_URL = "https://api.cmfchile.cl/api-sbifv3/recursos_api/uf"

async def get_valor_uf():
    hoy = date.today()
    url = f"{BASE_URL}/{hoy.year}/{hoy.month:02d}/dias/{hoy.day}?apikey={API_KEY}&formato=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        valor_uf = response.json()
        valor = valor_uf["UFs"][0]["Valor"]
        mensaje = f"A día de hoy el valor de la UF ha alcanzado el valor de {valor} pesos"
        return mensaje
    
    


    