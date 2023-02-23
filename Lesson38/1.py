def dels(num):
    dels = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dels.add(i)
            dels.add(num//i)
    return dels

for i in range(174457, 174505 + 1):
    d = dels(i)
    if len(d) == 2:
        print(*d)