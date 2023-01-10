# чувствую, что можно было проще сделать, но вроде работает

n = int(input())
str0 = ""
output = ""
while n > 0:
    str0 += str(n % 10)
    n //= 10

for i in range(len(str0)):
    if str0[i] == str0[0]:
        output = "YES"
    else:
        output = "NO"

print(output)
