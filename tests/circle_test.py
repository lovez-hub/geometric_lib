import math
import pytest
from geometric_lib.circle import *

def test_circle_area_positive():
    radius = 5
    expected = math.pi * radius ** 2

    result = area(radius)

    assert math.isclose(result, expected, rel_tol=1e-9)


def test_circle_perimeter_positive():

    radius = 5
    expected = 2 * math.pi * radius

    result = perimeter(radius)
    assert math.isclose(result, expected, rel_tol=1e-9)

def test_circle_area_negative_radius():
    radius = -5
    with pytest.raises(ValueError) as excinfo:
        area(radius)
    assert "The parties must be positive." not in str(excinfo.value)


def test_circle_perimeter_negative_radius():
    radius = -5

    with pytest.raises(ValueError):
        perimeter(radius)
