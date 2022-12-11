# print(input().replace(" ", "\n"))

s = input()
for i in range(len(s)):
    if s[i] == " ":
        s = s[:i] + "\n" + s[i+1:]

print(s)

