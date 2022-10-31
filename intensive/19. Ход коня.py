x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

if (y1 + 2 == y2 or y1 - 2 == y2) and (x1 + 1 == x2 or x1 - 1 == x2):
    print("YES")
elif (x1 + 2 == x2 or x1 - 2 == x2) and (y1 + 1 == y2 or y1 - 1 == y2):
    print("YES")
else:
    print("NO")
