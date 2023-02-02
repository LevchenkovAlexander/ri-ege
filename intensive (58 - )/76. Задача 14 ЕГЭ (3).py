a = 572
summ = 0
for i in range(2,11):
    n = a
    s = ""
    flag = False
    while n:
        s = str(n % i) + s
        n //= i
    print(s, i)
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            flag = True
    if flag: summ += i
print(summ)