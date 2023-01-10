a = int(input())

if (a // 1000 < 10 and a // 1000 >= 1) and (a % 7 == 0 or a % 17 == 0):
    print("YES")
else:
    print("NO")

