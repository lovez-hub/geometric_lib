import math


def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The parties must be positive.")
    s = (a + b + c) / 2
    if s <= a or s <= b or s <= c:
        raise ValueError("A triangle is not created with such sides.")
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The parties must be positive.")
    return a + b + c

