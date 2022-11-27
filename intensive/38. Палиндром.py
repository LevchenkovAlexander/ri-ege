n = int(input())

is_pol = True
k = 0
tmp = n

while tmp > 0:
    tmp //= 10
    k += 1

_len = k

while k > 0:
    if (n % 10) != (n // 10**(k - 1)):
        is_pol = False
        break
    n = n % 10**(k - 1)
    n //= 10
    k -= 2

print(is_pol)
