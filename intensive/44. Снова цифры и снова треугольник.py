n = int(input())
tr = ""
tmp = ""
j = ""
for i in range(1, n+1):
    tmp = ""
    for k in range(1, i+1):
        tmp += str(k)
    tr += tmp
    tmp = tmp[::-1]
    tmp = tmp[1:]
    tr += tmp + "\n"

print(tr)
