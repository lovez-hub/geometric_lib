import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    """
    Рассчитывает и выводит результат вычисления периметра или площади фигуры.

    Функция проверяет, принадлежит ли фигура и функция к спискам допустимых фигур
    и функций. После этого выполняет вызов метода соответствующей фигуры для 
    вычисления периметра или площади.

    Args:
        fig (str): Название фигуры ('circle' или 'square').
        func (str): Название функции ('perimeter' или 'area').
        size (list): Размеры фигуры. Для круга это радиус, для квадрата – сторона.

    Raises:
        AssertionError: Если фигура не из списка допустимых фигур.
        AssertionError: Если функция не из списка допустимых функций.

    Example:
        >>> calc('circle', 'area', [5])
        area of circle is 78.54
    """
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    """
    Основной блок программы для взаимодействия с пользователем.

    Пользователь вводит фигуру, функцию (площадь или периметр), а также 
    размеры фигуры. После этого вызывается функция calc для расчёта и вывода
    результата.

    - Фигура и функция проверяются на принадлежность к спискам figs и funcs.
    - Размеры вводятся в зависимости от выбранной фигуры и функции.

    Raises:
        ValueError: Если размеры введены некорректно (не целые числа).
    """
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    """
    Рассчитывает и выводит результат вычисления периметра или площади фигуры.

    Функция проверяет, принадлежит ли фигура и функция к спискам допустимых фигур
    и функций. После этого выполняет вызов метода соответствующей фигуры для 
    вычисления периметра или площади.

    Args:
        fig (str): Название фигуры ('circle' или 'square').
        func (str): Название функции ('perimeter' или 'area').
        size (list): Размеры фигуры. Для круга это радиус, для квадрата – сторона.

    Raises:
        AssertionError: Если фигура не из списка допустимых фигур.
        AssertionError: Если функция не из списка допустимых функций.

    Example:
        >>> calc('circle', 'area', [5])
        area of circle is 78.54
    """
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    """
    Основной блок программы для взаимодействия с пользователем.

    Пользователь вводит фигуру, функцию (площадь или периметр), а также 
    размеры фигуры. После этого вызывается функция calc для расчёта и вывода
    результата.

    - Фигура и функция проверяются на принадлежность к спискам figs и funcs.
    - Размеры вводятся в зависимости от выбранной фигуры и функции.

    Raises:
        ValueError: Если размеры введены некорректно (не целые числа).
    """
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)

