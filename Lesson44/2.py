def add(x):
    return int(str(x) + "1")


def f(x, y):
    if x > y: return 0
    if x == y: return 1
    n = add(x)
    return f(x+1, y) + (f(n, y) if n % 3 == 0 else 0 )+ f(x*5, y)


print(f(1, 410))