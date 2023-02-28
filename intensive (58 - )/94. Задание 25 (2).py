def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def F(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i): divs.add(i)
            if is_prime(num//i): divs.add(num//i)
    return (sum(divs)//len(divs)) if len(divs) else 0


n = 650000
count = 0
while count < 4:
    f = F(n)
    if f % 37 == 23:
        count += 1
        print(n, f)
    n += 1