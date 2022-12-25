from itertools import permutations


def check(n):
    for i in range(len(n)-1):
        if (n[i] in "0246" and n[i + 1] in "0246") or (n[i] in "1357" and n[i + 1] in "1357") or n[-1] not in "05" or n[0] == "0":
            return False
    return True


p = [''.join(i) for i in permutations("0123456789", 6)]
cnt = 0
for i in p:
    if check(i):
        cnt += 1
        print(i)
print(cnt)
