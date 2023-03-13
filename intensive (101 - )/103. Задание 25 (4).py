def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return 0
    return 1


def sum_divs(num):
    d = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i): d.add(i)
            if is_prime(num//i): d.add(num//i)
    return sum(d) if len(d) else 0


count = 0
a = 250000
while count < 5:
    s = sum_divs(a)
    if s % 17 == 0 and s != 0:
        count += 1
        print(a, s)
    a += 1
