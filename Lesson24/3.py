from itertools import product


def good(s):
    return s.count("в") <= 1 and s[0] != "ш" and s[-1] not in "ия"


alf = "вишня"
cnt = 0
p = [''.join(i) for i in product(alf, repeat=6)]
for i in p:
    if good(i):
        cnt += 1
print(cnt)
