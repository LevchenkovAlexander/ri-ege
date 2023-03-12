def f(x, y):
    if x < y: 
        return 0
    if x == y:
        return 1
    return f(x-1, y) + f(x - 3, y) + (f(x//3, y) if x % 3 == 0 else 0)


print(f(22, 2))