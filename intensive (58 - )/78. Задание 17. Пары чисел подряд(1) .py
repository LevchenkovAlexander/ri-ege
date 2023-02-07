file = open('files\\78.txt')

a = list(map(int, file))
p = []

for i in range(len(a) - 1):
    if (a[i] % 171 == 0 or a[i + 1] % 171 == 0) and (a[i] % 2 or a[i + 1] % 2):
        p.append(a[i] + a[i + 1])
print(len(p), max(p))
 