x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

if x == x1 or y == y1:
    print("YES")
elif x == x1 and y == y1:
    print("Error: same spot")
else:
    print("NO")
