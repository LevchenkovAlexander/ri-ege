s = input()
output = "YES"
for i in range(s.__len__()-1):
    if s[i] < s[i+1]:
        output = "NO"

print(output)
