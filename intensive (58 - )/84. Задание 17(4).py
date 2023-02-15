file = open("files\\84.txt")
a = list(map(int, file))
n = len(a)
p = []

for i in range(n):
    for j in range(i + 1, n):
        if (a[i]+a[j]) % 8 == 0:
            p.append(a[i]+a[j])
            
print(len(p), max(p))