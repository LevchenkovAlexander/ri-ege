def dels(num):
    dels_beg = []
    dels_end = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dels_beg.append(i)
            dels_end.append(num//i)
            if i**2 == num: dels_end.pop()
    return dels_beg + dels_end[::-1]


for i in range(110203, 110245 + 1):
    d = dels(i)
    if len(d) == 4:
        print(*d)