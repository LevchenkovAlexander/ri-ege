s = input()
output = ""

for i in range(len(s)):
    if i % 2 == 0:
        output += s[i] + "\n"
print(output)
