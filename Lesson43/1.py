def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x == 21:
        return 0
    return f(x+1, y) + f(x*2 + 1, y)


print(f(1, 25))