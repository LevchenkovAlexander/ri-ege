from sys import setrecursionlimit

setrecursionlimit(2500)


def f(n):
    if n < 4 or n % 2:
        return 1
    return f(n-1) + f(n-2) + f(n-3)


print(f(2008) - f(2006))