from geometric_lib import circle
from geometric_lib import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'circle': 1,
    'square': 1
}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure '{fig}'. Available figures: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function '{func}'. Available functions: {funcs}")

    expected_size = sizes.get(fig)
    if len(size) != expected_size:
        raise ValueError(f"{fig} {func} expects {expected_size} arguments, got {len(size)}")

    module = globals()[fig]
    if not hasattr(module, func):
        raise AttributeError(f"Module '{fig}' has no function '{func}'")

    result = getattr(module, func)(*size)
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(fig, 1):
        try:
            size = list(map(float, input("Input figure sizes separated by space:\n").split()))
        except ValueError:
            print("Please enter valid numbers.")
            size = []

    try:
        result = calc(fig, func, size)
        print(f'{func} of {fig} is {result}')
    except Exception as e:
        print(f"Error: {e}")
