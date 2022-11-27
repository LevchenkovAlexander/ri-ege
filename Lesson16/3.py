n = int(input())
out = ""
for i in range(1, n+1):
    for j in range(i):
        out += str(i)
    out += "\n"
print(out)
