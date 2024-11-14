import pytest
from geometric_lib import circle
from geometric_lib import square
from geometric_lib.calculate import calc


def test_circle_area():
    fig = "circle"
    func = "area"
    size = [5]
    expected = circle.area(5)
    result = calc(fig, func, size)
    assert result == expected


def test_circle_per():
    fig = "circle"
    func = "perimeter"
    size = [5]
    expected = circle.perimeter(5)
    result = calc(fig, func, size)
    assert result == expected


def test_square_area():
    fig = "square"
    func = "area"
    size = [4]
    expected = square.area(4)
    result = calc(fig, func, size)
    assert result == expected


def test_square_per():
    fig = "square"
    func = "perimeter"
    size = [4]
    expected = square.perimeter(4)
    result = calc(fig, func, size)
    assert result == expected


def test_invalid_fig():
    fig = "hexagon"
    func = "area"
    size = [6]
    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_invalid_func():
    fig = "circle"
    func = "volume"
    size = [5]
    with pytest.raises(AssertionError):
        calc(fig, func, size)
