from itertools import permutations


def check(n):
    for i in range(len(n)-1):
        if ((n[i] in "0246" and n[i+1] in "0246") or (n[i] in "1357" and n[i+1] in "1357")) or n[0] == "0":
            return False
    return True


cnt = 0
p = [''.join(i) for i in permutations("01234567", 5)]

for i in p:
    if check(i):
        cnt += 1
        print(i)
print(cnt)
