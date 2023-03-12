def exec(char, num):
    if char == "1":
        return num + 1
    if char == "2":
        return num + 2
    return num * 2


def alg(s):
    num = 1
    for i in s:
        num = exec(i, num)
    return num

from itertools import product
count = 0
p = [''.join(i) for i in product("123", repeat= 6)]
for i in p:
    if alg(i) == 20:
        count += 1
        
print(count)