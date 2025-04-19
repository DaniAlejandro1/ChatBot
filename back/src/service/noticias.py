import httpx
import os
from dotenv import load_dotenv
from src.utils.response_format import ResponseFormat

load_dotenv()

API_KEY = os.getenv("NOTICIAS_API_KEY")
URL = f"https://newsapi.org/v2/top-headlines?apiKey={API_KEY}&language=en&sortBy=publishedAt"

async def get_noticias_recientes():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        response.raise_for_status()
        data = response.json()
        title = data["articles"][0]["title"]
        return title
