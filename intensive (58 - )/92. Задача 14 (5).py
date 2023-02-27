a = 622
sum = 0

for i in range(2, 11):
    n = a
    s = ""
    while n:
        s = str(n % i) + s
        n //= i
    if len(s) % 2 == 0: sum += i

print(sum)