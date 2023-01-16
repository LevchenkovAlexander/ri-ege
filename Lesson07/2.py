a, b, c = [float(i) for i in input().split()]

if a == b == c:
    Type = "Равносторонний"
elif a == b or a == c or b == c:
    Type = "Равнобедренный"
else:
    Type = "Разносторонний"

print(Type)
