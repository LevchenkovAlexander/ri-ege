s = open("files/125.txt").read()
alf = "ABEF"
count = mx = 0
for i in range(len(s)):
    if s[i] in alf:
        count += 1
        mx = max(mx, count)
    else:
        count = 0

print(mx)