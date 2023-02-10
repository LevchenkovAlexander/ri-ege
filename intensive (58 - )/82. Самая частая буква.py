s = input()
m = s[0]

for i in range(len(s)):
    m = s[i] if s.count(s[i]) > s.count(m) else m

s = s.replace(m, '*')
print(s)
