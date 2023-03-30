def a(n):
    for x in range(1000):
        for y in range(1000):
            if ((x > 4) or (x + 2 < y) or (x**2 + y**2 < n)) == 0:
                return 0
    return 1


n = 0

while 1:
    if a(n):
        print(n)
        break
    n += 1