n = int(input())
_del = n
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        _del = i
        break
print(_del)

