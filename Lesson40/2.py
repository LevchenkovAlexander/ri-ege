def divs_f(num):
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    print(len(divs))