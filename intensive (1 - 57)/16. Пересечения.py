a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < a2:
    if a1 < a2 and b1 > b2:
        print("пересечение: [ ", a2, "; ", b2, " ]")
    elif b1 > a2:
        print("пересечение: [ ", a2, "; ", b1, " ]")
    elif b1 == a2:
        print("общая точка - ", b1)
    else:
        print("пустое множество")

else:
    if a2 < a1 and b2 > b1:
        print("пересечение: [ ", a1, "; ", b1, " ]")
    elif b2 > a1:
        print("пересечение: [ ", a1, "; ", b2, " ]")
    elif b2 == a1:
        print("общая точка - ", b1)
    else:
        print("пустое множество")
