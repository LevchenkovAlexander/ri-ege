def a(n):
    for x in range(1000):
        if ((x & n == 0) or ((x & 69) <= (x & 118 == 6))) == 0:
            return 0
    return 1


n = 1

while 1:
    if a(n):
        print(n)
        break
    n += 1