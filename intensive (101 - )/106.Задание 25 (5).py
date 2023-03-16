def check(num):
    divs_beg = []
    divs_end = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs_beg.append(i)
            divs_end.append(num//i)
            if i ** 2 == num: divs_end.pop()
    for i in divs_beg + divs_end[::-1]:
        if str(i)[-1] == "8" and i != 8:
            return i
    return 0
        
        
a = 500000
count = 0

while count < 5:
    res = check(a)
    if res:
        print(a, res)
        count += 1
    a += 1