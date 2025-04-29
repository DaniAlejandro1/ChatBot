import pytest
import asyncio
import os
import aiohttp


from src.service.clima import get_clima
from src.service.dolar import get_valor_dolar
from src.service.uf import get_valor_uf
from src.service.noticias import get_noticias_recientes
from src.utils.modelo_ia import detectar_intencion, parafrasear_texto


CLIMA_API_KEY = os.getenv('API_KEY')
NEWS_API_KEY = os.getenv('NOTICIAS_API_KEY')
UF_API_KEY = os.getenv("CMF_API_KEY")

# --- Tests existentes basados en funciones reales ---

# T-01: Consultar API del clima
@pytest.mark.asyncio
async def test_get_clima():
    resultado = await get_clima("Temuco")
    assert isinstance(resultado, str)
    assert "°C" in resultado

# T-02: Test de conexión a API del clima
@pytest.mark.asyncio
async def test_conexion_weatherapi():
    url = f"http://api.weatherapi.com/v1/current.json?q=Temuco&key={CLIMA_API_KEY}"
    response = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                response = response.status
    except Exception:
        response = False
    assert response is 200

# T-03: Consultar valor del dólar
@pytest.mark.asyncio
async def test_get_valor_dolar():
    resultado = await get_valor_dolar()
    assert resultado.isdigit()
    assert int(resultado) > 0

# T-04: Test de conexión a API del dólar
@pytest.mark.asyncio
async def test_conexion_dolarapi():
    url = "https://api.exchangerate.host/latest?base=USD"
    resultado = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                resultado =  response.status
    except Exception:
        resultado =  response.status
    
    assert resultado is 200

# T-05: Consultar valor de UF
@pytest.mark.asyncio
async def test_get_valor_uf():
    resultado = await get_valor_uf()
    resultado = resultado.replace(".", "").replace(",", "")
    assert resultado.isdigit()
    assert int(resultado) > 0

# T-06: Test de conexión a API de UF
@pytest.mark.asyncio
async def test_conexion_ufapi():
    url = f"https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey={UF_API_KEY}"
    resultado = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
               resultado = response.status
    except Exception:
         resultado = response.status
    assert resultado is 200


# T-07: Consultar noticia
@pytest.mark.asyncio
async def test_get_noticias_recientes():
    resultado = await get_noticias_recientes()
    assert isinstance(resultado, str)
    assert len(resultado) > 0


# T-08: Test de conexión a API de noticias
@pytest.mark.asyncio
async def test_conexion_newsapi():
    url = f"https://newsapi.org/v2/top-headlines?country=cl&apiKey={NEWS_API_KEY}"
    resultado = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                resultado = response.status
    except Exception:
        resultado = response.status
    assert resultado is 200


# T-10: Obtener intención de mensaje de usuario



# T-11: Reconocer intencion de conocer clima
@pytest.mark.asyncio
async def test_reconocer_intencion_clima():
    texto = "Quiero saber el clima en Temuco"
    resultado = detectar_intencion(texto)
    assert resultado in "clima"

# T-12: Reconocer intencion de conocer el valor del dólar
@pytest.mark.asyncio
async def test_reconocer_intencion_dolar():
    texto = "Quiero saber el valor del dolar"
    resultado = detectar_intencion(texto)
    assert resultado in "dolar"

# T-13: Reconocer intencion de conocer el valor de la UF
@pytest.mark.asyncio
async def test_reconocer_intencion_uf():
    texto = "Quiero saber el valor de la uf"
    resultado = detectar_intencion(texto)
    assert resultado in "uf"

# T-14: Reconocer intencion de conocer una noticia
@pytest.mark.asyncio
async def test_reconocer_intencion_noticias():
    texto = "Quiero una noticia"
    resultado = detectar_intencion(texto)
    assert resultado in "noticias"

# T-16 Comprobar conexion con Cohere
@pytest.mark.asyncio
async def test_conexion_cohere():
    respuesta = 0
    url = "https://api.cohere.ai/generate"
    headers = {
        "Authorization": "Bearer z0U0usZ1wAOKCGr5JN83d9neMj4YA4KEHLeZ5OUX"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={}, headers=headers, timeout=10) as response:
                # Check if the response status is one of the expected codes
                assert response.status in [200, 400, 401], f"Unexpected status code: {response.status}"
    except aiohttp.ClientError as e:
        pytest.fail(f"Connection failed: {str(e)}")
    except asyncio.TimeoutError:
        pytest.fail("Request timed out")


# T-17 Parafrasear valor de la UF
@pytest.mark.asyncio
async def test_parafrasear_uf():
    topico = "uf"
    valor = "30.000"
    resultado = parafrasear_texto(topico, valor)
    assert "30.000" in resultado or "Treinta mil" in resultado


# T-18 Parafrasear valor del clima
@pytest.mark.asyncio
async def test_parafrasear_clima():
    topico = "clima"
    valor = "15°C"
    resultado = parafrasear_texto(topico, valor)
    assert "15" in resultado


# T-19 Parafrasear valor del dolar
@pytest.mark.asyncio
async def test_parafrasear_dolar():
    topico = "dolar"
    valor = "936"
    resultado = parafrasear_texto(topico, valor)
    assert "dolar" in resultado and "936" in resultado or "936" in resultado
