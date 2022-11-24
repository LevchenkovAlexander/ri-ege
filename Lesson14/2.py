s = input()
output = "No"
i = 0

while i < len(s):
    if s[i] == "9":
        output = "Yes"
        break
    i += 1
print(output)
