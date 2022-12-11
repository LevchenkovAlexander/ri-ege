s = input()
point1 = 0
f = False
point2 = 0

for i, sym in enumerate(s):
    if sym == "p" and not f:
        point1 = i
        f = True
    elif sym == "p" and f:
        point2 = i
s1 = s[:point1]
s2 = s[point2+1:]
s = s1 + s2
print(s)
