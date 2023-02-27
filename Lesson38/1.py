def dels(num):
    dels_beg = []
    dels_end = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dels_beg.append(i)
            dels_end.append(num//i)
    return dels_beg + dels_end[::-1 ]

for i in range(174457, 174505 + 1):
    d = dels(i)
    if len(d) == 2:
        print(*d)