s = open("files/118.txt").read()
d = [1 for i in s]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        d[i] = d[i-1] + 1

for i in range(len(d)):
    if d[i] == max(d):
        print(f"\'{s[i]}\'", d[i])