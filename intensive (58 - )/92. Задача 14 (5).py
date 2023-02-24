a = 622
count = 0

for i in range(2, 11):
    n = a
    s = ""
    while n:
        s = str(n % i) + s
        n //= i
    if len(s) % 2 == 0: count += 1

print(count)