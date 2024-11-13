import math
import pytest
from geometric_lib.triangle import area, perimeter


def test_triangle_area_valid():
    a, b, c = 3, 4, 5
    expected = 6.0

    result = area(a, b, c)

    assert math.isclose(result, expected, rel_tol=1e-9)


def test_triangle_perimeter_valid():
    a, b, c = 3, 4, 5
    expected = 12

    result = perimeter(a, b, c)

    assert result == expected


def test_triangle_area_invalid_sides():
    a, b, c = 1, 2, 3

    with pytest.raises(ValueError):
        area(a, b, c)


def test_triangle_perimeter_negative_side():
    a, b, c = -3, 4, 5

    with pytest.raises(ValueError):
        perimeter(a, b, c)
