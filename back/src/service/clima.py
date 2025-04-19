import os
from dotenv import load_dotenv
import httpx

load_dotenv()
API_KEY = os.getenv('API_KEY')

BASE_URL = "http://api.weatherapi.com/v1/current.json"

async def get_clima(ciudad: str):
    params = {
        "key": API_KEY,
        "q": ciudad
    }

    async with httpx.AsyncClient() as client:

            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()

            data = response.json()


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
