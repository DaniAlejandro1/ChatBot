import pytest
import _asyncio

from src.service.clima import get_clima
from src.service.dolar import get_valor_dolar
from src.service.uf import get_valor_uf
from src.service.noticias import get_noticias_recientes

@pytest.mark.asyncio
async def test_get_clima():
    resultado = await get_clima("Temuco")
    assert isinstance(resultado, str), "El resultado debe ser una cadena de texto"
    assert "°C" in resultado


@pytest.mark.asyncio
async def test_get_valor_dolar():
    resultado = await get_valor_dolar()
    assert resultado.isdigit()  # valor redondeado en string
    assert int(resultado) > 0


@pytest.mark.asyncio
async def test_get_noticias_recientes():
    resultado = await get_noticias_recientes()
    assert isinstance(resultado, str)
    assert len(resultado) > 0


@pytest.mark.asyncio
async def test_get_valor_uf():
    resultado = await get_valor_uf()
    resultado = resultado.replace(".", "").replace(",", "")
    assert resultado.isdigit()
    assert int(resultado) > 0

