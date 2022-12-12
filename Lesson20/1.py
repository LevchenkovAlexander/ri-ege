s = input()
if len(s) % 2 == 0:
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
else:
    s1 = s[:len(s)//2+1]
    s2 = s[len(s)//2+1:]


print(s2, s1)
