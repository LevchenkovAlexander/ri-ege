file = open("17.6.txt")
a = list(map(int, file))
n = len(a)
p = []

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0): 
            p.append(a[i] + a[j])
print(len(p), max(p))