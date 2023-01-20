s = input()
a = []
tmp = ""
for i in range(len(s)):
    if s[i] != " ":
        tmp += s[i]
    if i == len(s) - 1 or s[i] == " ":
        a.append(int(tmp)) 
        tmp = ""
a.sort()
print(a)
print(a[::-1])
