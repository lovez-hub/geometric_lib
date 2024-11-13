import math
import pytest
from geometric_lib.calculate import calc


def test_calc_circle_area():
    fig = 'circle'
    func = 'area'
    size = [5]
    expected = math.pi * 5 ** 2

    result = calc(fig, func, size)

    assert math.isclose(result, expected, rel_tol=1e-9)


def test_calc_square_perimeter():
    fig = 'square'
    func = 'perimeter'
    size = [4]
    expected = 16

    result = calc(fig, func, size)

    assert result == expected

def test_calc_invalid_figure():
    fig = 'hexagon'
    func = 'area'
    size = [6]

    with pytest.raises(ValueError) as excinfo:
        calc(fig, func, size)
    assert "Invalid figure" in str(excinfo.value)


def test_calc_invalid_function():
    fig = 'circle'
    func = 'volume'
    size = [5]

    with pytest.raises(ValueError) as excinfo:
        calc(fig, func, size)
    assert "Invalid function" in str(excinfo.value)

def test_calc_non_numeric_size():
    fig = 'circle'
    func = 'area'
    size = ['a']

    with pytest.raises(TypeError):
        calc(fig, func, size)
