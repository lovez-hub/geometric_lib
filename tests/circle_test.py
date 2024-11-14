import math
import pytest
from geometric_lib.circle import area,perimeter

def test_area_positive():
    radius = 5
    expected = math.pi * radius ** 2

    result = area(radius)

    assert math.isclose(result, expected, rel_tol=1e-9)


def test_per_positive():

    radius = 5
    expected = 2 * math.pi * radius

    result = perimeter(radius)
    assert math.isclose(result, expected, rel_tol=1e-9)

def test_negative_r_area():
    radius = -5
    with pytest.raises(ValueError) as excinfo:
        area(radius)
    assert "The parties must be positive." not in str(excinfo.value)


def test_negative_r_per():
    radius = -5

    with pytest.raises(ValueError):
        perimeter(radius)
