def f(n):
    if n == 0: return 5
    if n > 0 and n % 2 == 0: 
        return 1 + f(n / 2)
    return f(n//2)


count = 0
for i in range(1, 1000000 + 1):
    if f(i) == 7: count += 1

print(count)