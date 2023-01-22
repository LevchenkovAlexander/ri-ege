a = [1, 3, 5, 8, 22, 14, 98, 11, 3, -5, -49, 17, 129, -14, -879, 150]
print(len(a))
print(a[0])
print(*a[::-1])
print("YES" if (3 in a and 879 in a) else "NO")
print(*[i for i in a if i < 0])
