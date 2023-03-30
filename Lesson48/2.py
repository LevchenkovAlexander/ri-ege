def a(n):
    for x in range(1000):
        for y in range(1000):
            if (((x - 20 < n) and (10 - y < n)) or ((x + 4) * y > 45)) == 0:
                return 0
    return 1


n = 0

while 1:
    if a(n):
        print(n)
        break
    n += 1