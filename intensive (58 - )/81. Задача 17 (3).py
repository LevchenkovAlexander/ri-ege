def check(s):
    for i in range(len(s) - 1):
        if s[i] % 2 == s[i + 1] % 2:
            return False
    return True


file = open("files/81.txt")

a = list(map(int, file))
p = []

for i in range(len(a) - 3):
    if check(a[i:i+4]):
        p.append(sum(a[i:i+4]))
print(len(p), max(p))