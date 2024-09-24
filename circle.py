import math


def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга, рассчитанная по формуле π * r^2.

    Example:
        >>> area(5)
        78.54
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр (окружность) круга по заданному радиусу.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Периметр круга, рассчитанный по формуле 2 * π * r.

    Example:
        >>> perimeter(5)
        31.42
    """
    return 2 * math.pi * r

