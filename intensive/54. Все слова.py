s = input()

output = ""

for i in range(s.count(" ") + 1):
    k = s.find(" ")
    if k != -1:
        output = s[:k]
        s = s[k + 1:]
    else:
        output = s
    print(output[::-1])
