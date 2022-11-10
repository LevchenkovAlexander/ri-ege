m, p, n = [int(i) for i in input().split()]

p = 1 + (p/100)

for i in range(1, n + 1):
    m *= p
    print(m)


