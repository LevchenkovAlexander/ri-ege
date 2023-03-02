def divs_f(num):
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return len(divs)


while 1: print(divs_f(int(input())))