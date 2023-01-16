from math import ceil

n = int(input())

n1 = ceil(n ** 0.5)

d0 = n
d1 = 0
d2 = 0
c = 0

for i in range(1, n1+1):
    if n % i == 0:
        c += 2
        if i > 1 and n // i > d2:
            if n // i > d1:
                d2 = d1
                d1 = n // i
            else:
                d2 = n // i
    if i == n ** 0.5:
        c -= 1
print(c, d0, d1, d2)
