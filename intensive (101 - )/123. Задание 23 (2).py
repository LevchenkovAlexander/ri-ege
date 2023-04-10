def add(x):
    return x + (x + 1 if x % 2 else x + 2)


def f(x, y):
    if x > y or x == 21:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 4, y) + f(add(x), y)


print(f(2, 11) * f(11, 26))