def f(x, y, count):
    if x == y and count < 4:
        return 1
    if x >= y:
        return 0
    
    return f(x+2, y, count if (x+2)%2 else count + 1) + f(x * 2, y, count if (x+2)%2 else count + 1) + f(x*3, y, count if (x+2)%2 else count + 1)


print(f(1, 402, 0))