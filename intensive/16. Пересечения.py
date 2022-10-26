a1, b1 = [int(i) for i in input().split()]
a2, b2 = [int(i) for i in input().split()]

if b1 > a2:
    print("пересечение: [ ", a2, "; ", b1, " ]")
elif b1 == a2:
    print("пересечение - ", b1)
else:
    print("пересечения нет")
