def div_sum(n):
    divs = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs += i
            if i ** 2 != n:
                divs += n//i
    return divs


from fnmatch import fnmatch

count = i = 0
while count < 7:
    if fnmatch(str(i), "?6*6*?6") and i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
        print(i, div_sum(i))
        count += 1
    i += 1