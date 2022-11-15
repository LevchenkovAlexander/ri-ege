n = int(input())

_sum = 0
k = 0

for i in range(n):
    x = int(input())
    if 99 < x < 1000 and x % 2 != 0:
       _sum += x
       k += 1

print(_sum/k)

