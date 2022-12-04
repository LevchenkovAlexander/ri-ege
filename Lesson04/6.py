a = int(input())
b = int(input())
c = int(input())
tmp = int(0)
i = 0
for i in range(2):
    if a > b:
        tmp = a
        a = b
        b = tmp
    elif b > c:
        tmp = b
        b = c
        c = tmp

print(a, b, c)
