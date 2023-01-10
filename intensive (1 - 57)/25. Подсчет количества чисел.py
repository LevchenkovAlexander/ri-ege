a = int(input())
b = int(input())

s = 0

for i in range(a, b+1):
    j = i**3
    if j % 10 == 4 or j % 10 == 9:
        s += 1

print(s)

