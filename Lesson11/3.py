from math import floor, sqrt

num0 = int(input())

res = 0
num = floor(sqrt(num0))

for i in range(1, num+1):
    if num % i == 0 and i != sqrt(num0):
        res += i
        res += num0 / i
    elif i == sqrt(num0):
        res += i

print(int(res))
