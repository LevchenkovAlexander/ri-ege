from itertools import product


def good(s):
    flag = True
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            flag = False
    return s[0] != "а" and flag


alf = "абвгд"
cnt = 0
p = [''.join(i) for i in product(alf, repeat=6)]

for i in p:
    if good(i):
        cnt += 1
print(cnt)
