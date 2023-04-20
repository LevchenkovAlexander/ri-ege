def check(n):
    bn = bin(n)[2:]
    return n % 3 == 0 and n % 11 == 0 and bn.count("0") == 5 and bn[-1] == "1"


ans = []
for i in range(10, 10000):
    if check(i):
        ans.append(i)
print(len(ans), max(ans))