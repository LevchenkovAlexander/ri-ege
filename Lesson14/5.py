n = int(input())
n = str(n)

_min = float("inf")
_max = float("-inf")
i = 0

while i < len(n):
    if int(n[i]) > _max:
        _max = int(n[i])
    elif int(n[i]) < _min:
        _min = int(n[i])
    i += 1

print("max num", _max)
print("min num", _min)
