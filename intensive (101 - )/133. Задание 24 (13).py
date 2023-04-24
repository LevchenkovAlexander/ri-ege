s = open("files/133.txt").read()
d = [1 for i in range(len(s))]

for i in range(1, len(s)):
    if s[i-1] + s[i] != "QW":
        d[i] = d[i-1] + 1

print(max(d))