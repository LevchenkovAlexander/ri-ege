s = open("files/122.txt").read()

s = ["g" if i in "AO" else "c" for i in s]
d = [0 for i in s]
if s[0] == "g": d[0] = 1
 
for i in range(1, len(s)):
    if s[i-1] + s[i] in "gcg":
        d[i] = d[i-1] + 1
print(max(d)//2)