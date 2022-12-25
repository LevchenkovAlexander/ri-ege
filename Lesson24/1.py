from itertools import product


def good(s):
    return s[0] in "ЗМ" and s[-1] in "ИА"


alf = "ЗИМА"

prod = [''.join(i) for i in product(alf, repeat=5)]

cnt = 0

for i in range(len(prod)):
    if good(prod[i]):
        cnt += 1
print(cnt)

