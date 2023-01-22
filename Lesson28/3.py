n = int(input())

a = []

for i in range(n):
    inp = input()
    if inp not in a:
        a.append(inp)

print(*a, sep= "\n")