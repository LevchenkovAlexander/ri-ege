from functools import cache

@cache
def f(x, y, en= 700):
    if x > y or en < 0:
        return 0
    if x == y and en == 0:
        return 1
    return f(x + 3, y, en-10) + f(x * 4, y, en-10) + f(x * 5, y, en-10)


print(f(1, 4400))