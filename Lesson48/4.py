def a(n):
    for x in range(1000):
        for y in range(1000):
            if ((2*x + 3*y != 72) or ((n > x) and (n > y))) == 0:
                return 0
    return 1


n = 0

while 1:
    if a(n):
        print(n)
        break
    n += 1