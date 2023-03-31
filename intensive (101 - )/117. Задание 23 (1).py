def minus(x):
    return bin(int(x, 2) - 1)[2:]
    

def func(x, y):
    if int(x, 2) < int(y, 2):
        return 0
    if x == y:
        return 1
    return func(minus(x), y) + func(x[:-1], y)


print(func("100001", "100"))