n = int(input())
_sum = 0
mul = 1
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        _sum += x
    else:
        mul *= x

if _sum > mul:
    res = _sum / mul
else:
    res = mul / _sum

print(res)
