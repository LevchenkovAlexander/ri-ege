def divs(n):
    div = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0: div.append(i)
            if (n // i) % 2 == 0 and i ** 2 != n: div.append(n // i)
    return div     


from fnmatch import fnmatch

cnt = 0
i = 65000
while cnt < 7:
    i += 1
    if fnmatch(str(i), "6*97*5?") and len(f := divs(i)) >= 4:
        cnt += 1
        print(i, sum(f))
