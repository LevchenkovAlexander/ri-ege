def triangle(a, b, c):
    return max(a, b, c) < (a + b + c - max(a, b, c))

while 1: print(triangle(int(input()), int(input()), int(input())))