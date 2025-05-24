from weather import weather_calculator
import pytest

def test_weather_calculator():
    assert weather_calculator(-5) == "Freezing"
    assert weather_calculator(5) == "Cold"
    assert weather_calculator(15) == "Warm"
    assert weather_calculator(25) == "Hot"
    assert weather_calculator(35) == "Very Hot"