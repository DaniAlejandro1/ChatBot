import httpx

async def get_valor_dolar():
    url = "https://api.appnexus.com/currency?code=CLP&show_rate=true"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        valor = data["response"]["currency"]["rate_per_usd"]
        valor_redondeado = str(round(float(valor)))
        mensaje = f"A día de hoy el valor del dolar ha alcanzado los {valor_redondeado} pesos"
        return valor_redondeado