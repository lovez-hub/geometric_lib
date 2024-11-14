from geometric_lib import circle
from geometric_lib import square

globals()["circle"] = circle
globals()["square"] = square

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {"circle": 1, "square": 1}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input("Input figure sizes separated by space\n").split(),
            )
        )
    print(calc(fig, func, size))
