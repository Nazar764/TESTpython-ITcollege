import pytest

from src.temperature_converter import TemperatureConverter


@pytest.mark.parametrize(
    "celsius, fahrenheit",
    [(0, 32), (100, 212), (-273.15, -459.67)],
)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert TemperatureConverter.celsius_to_fahrenheit(celsius) == pytest.approx(
        fahrenheit
    )


@pytest.mark.parametrize(
    "fahrenheit, celsius",
    [(32, 0), (212, 100), (-459.67, -273.15)],
)
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    assert TemperatureConverter.fahrenheit_to_celsius(fahrenheit) == pytest.approx(
        celsius
    )


@pytest.mark.parametrize(
    "converter, value",
    [
        (TemperatureConverter.celsius_to_fahrenheit, "0"),
        (TemperatureConverter.fahrenheit_to_celsius, "32"),
        (TemperatureConverter.celsius_to_fahrenheit, True),
        (TemperatureConverter.fahrenheit_to_celsius, False),
    ],
)
def test_converters_reject_non_numeric_values(converter, value):
    with pytest.raises(TypeError, match="Temperature must be a number"):
        converter(value)


@pytest.mark.parametrize(
    "converter, value",
    [
        (TemperatureConverter.celsius_to_fahrenheit, -273.16),
        (TemperatureConverter.fahrenheit_to_celsius, -459.68),
    ],
)
def test_converters_reject_temperature_below_absolute_zero(converter, value):
    with pytest.raises(ValueError, match="Temperature is below absolute zero"):
        converter(value)
