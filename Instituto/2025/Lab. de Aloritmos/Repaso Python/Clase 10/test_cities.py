import pytest
from city_functions import city_country

def test_city_country():
    """Verifica que la función retorna el formato correcto."""
    resultado = city_country("santiago", "chile")
    assert resultado == "Santiago, Chile"