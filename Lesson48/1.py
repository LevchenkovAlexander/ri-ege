def a(A):
    for x in range(1000):
        for y in range(1000):
            if ((x + y <= 22) or (y <= (x - 6)) or (y >= A)) == 0:
                return 0
    return 1


A = 5000

while A > -1:
    if a(A):
        print(A)
        break
    A -= 1