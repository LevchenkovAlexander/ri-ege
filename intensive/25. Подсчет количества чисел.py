a = int(input())
b = int(input())

s = 0

for i in range(a, b):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        s += 1

print(s)

