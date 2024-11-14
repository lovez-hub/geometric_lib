import pytest
from geometric_lib.square import area, perimeter


def test_area_positive():
    side = 4
    expected = side * side

    result = area(side)

    assert result == expected


def test_per_positive():
    side = 4
    expected = 4 * side

    result = perimeter(side)

    assert result == expected


def test_area_negative_side():
    side = -4

    with pytest.raises(ValueError):
        area(side)


def test_perimeter_negative_side():
    side = -4

    with pytest.raises(ValueError):
        perimeter(side)
