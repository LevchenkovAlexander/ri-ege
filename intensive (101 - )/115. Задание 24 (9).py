a = open("files/115.txt").read()
f = ["l" if i.isalpha() else "n" for i in a]

d = [1 if i == "l" else 0 for i in f]


for i in range(1, len(f)):
    if f[i-1] + f[i] in "lnl":
        d[i] = d[i-1] + 1
print(max(d))