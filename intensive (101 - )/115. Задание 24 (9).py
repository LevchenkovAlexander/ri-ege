a = open("files/115.txt").read()
f = ["0" if i.isalpha() else "1" for i in a]

c = mx = 0
fl = 1 if f[0] == 0 else 0
for i in range(1, len(f)):
    if fl == 1 and f[i-1] + f[i] in "010":
        c += 1
        mx = max(mx, c)
    elif fl == 1:
        c = 0
        fl = 0
    elif f[i] == "0":
        fl = 1
        c += 1
    else:
        c = 0
        fl = 0
print(mx)