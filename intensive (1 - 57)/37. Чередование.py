s = input()
output = "Yes"
for i in range(len(s)-1):
    if int(s[i]) % 2 == int(s[i+1]) % 2:
        output = "No"

print(output)
