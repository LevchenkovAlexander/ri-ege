x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")