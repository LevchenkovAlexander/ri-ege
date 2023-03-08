from math import ceil
n = int(input())

a = []

for i in range(1, n):
    cnt = 0
    for j in range(2, ceil(i**0.5)):
        if i % j == 0 and j ** 2 != i:
            cnt += 2
        elif i % j == 0 and j ** 2 == i:
            cnt += 1
    if cnt >= 2:
        a.append(i)
print(a)
