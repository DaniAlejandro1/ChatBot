import os
from dotenv import load_dotenv
import httpx

load_dotenv()
API_KEY = os.getenv('API_KEY')

BASE_URL = "http://api.weatherapi.com/v1/current.json"

async def get_clima(ciudad: str ):
    params = {
        "key": API_KEY,
        "q": ciudad
    }

    async with httpx.AsyncClient() as client:

            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()

            data = response.json()

            temperatura = data["current"]["temp_c"]
            respuesta = f"{round(float(temperatura))} °C"
            
            return respuesta
