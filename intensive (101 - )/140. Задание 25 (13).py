from fnmatch import fnmatch

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num != 1


def divs(num):
    divs_beg = []
    divs_end = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                divs_beg.append(str(i))
            if i ** 2 != num and is_prime(n := num//i):
                divs_end.append(str(n))
    return divs_beg + divs_end[::-1]

    
count = 0
a = 4679000
while count < 5:
    f = "".join(d := divs(a))
    if fnmatch(f, "27*39?") or fnmatch(f, "34*2?7"):
        print(a, d[-1])
        count += 1
    a += 1