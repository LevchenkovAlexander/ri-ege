s = input()
max_l = 1
l = 0
f = ""

for i in range(len(s)):
    if s[i] == "A":
        l += 1
        f = "A"
    elif s[i] == "B" and f == "A":
        l += 1
        f = "B"
    else:
        l = 0

    max_l = l if max_l < l else max_l
print(max_l)
