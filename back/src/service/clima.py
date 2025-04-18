import os
from dotenv import load_dotenv
import httpx

load_dotenv()
API_KEY = os.getenv('API_KEY')

BASE_URL = "http://api.weatherapi.com/v1/current.json"

async def get_weather(ciudad: str):
    params = {
        "key": API_KEY,
        "q": ciudad
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()  # Esto levantará un error si el status es 4xx o 5xx

            # Procesamos la respuesta en formato JSON
            data = response.json()

            # Ajustamos la respuesta al formato esperado
            return {
                "location": {
                    "name": data["location"]["name"],
                    "country": data["location"]["country"]
                },
                "current": {
                    "temp_c": data["current"]["temp_c"],
                    "condition": {
                        "text": data["current"]["condition"]["text"],
                        "icon": data["current"]["condition"]["icon"]
                    }
                }
            }

        except httpx.RequestError as e:
            return {"error": f"Hubo un error en la solicitud al servicio de clima: {str(e)}"}

        except httpx.HTTPStatusError as e:
            return {"error": f"Error al obtener los datos del clima, código de estado: {e.response.status_code}"}