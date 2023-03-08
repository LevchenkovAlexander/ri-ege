s = open("files\\86.txt").read()

d = [1 for i in s]

for i in range(1, len(s)):
    if s[i-1]+s[i] not in "KLK": d[i] = d[i - 1] + 1

print(max(d))
