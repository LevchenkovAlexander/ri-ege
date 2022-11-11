from math import sqrt, floor

n = int(input())

n1 = floor(sqrt(n))

d0 = n
d1 = 0
d2 = 0
c = 0

for i in range(1, n1+1):
    if n1 % i == 0:
        c += 2
        if i > 1 and n // i > d2:
            if n // i > d1:
                d2 = d1
                d1 = n // i
            else:
                d2 = n // i

    if i == sqrt(n):
        c -= 1


print(c, d0, d1, d2)
