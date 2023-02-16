s = open("files\\86.txt").read()

d = [1 if (i != "K" and i != "L") else 0 for i in s]

for i in range(1, len(s)):
    if s[i] != "K" and s[i] != "L": d[i] = d[i - 1] + 1
    
print(max(d))
