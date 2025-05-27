import pytest
from main import sumar

@pytest.fixture
def datos_de_prueba():
    return (3, 5)

def test_sumar(datos_de_prueba):
    a, b = datos_de_prueba
    resultado = sumar(a, b)