def pal(n):
    return str(n[0]) == str(n[0])[::-1]


def divs(n):
    divs_beg = []
    divs_end = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs_beg.append(i)
            divs_end.append(n//i)
    divs_ = divs_beg + divs_end[::-1]
    return [sum(divs_), divs_[-2]]


count = 0
num = 520000
while count < 5:
    d = divs(num)
    if pal(d):
        print(num, d[1])
        count += 1
    num += 1
