def f(x, y):
    if x > y or x == 21:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 3, y) + f(x * 4, y)


print(f(2, 16) * f(16, 60))