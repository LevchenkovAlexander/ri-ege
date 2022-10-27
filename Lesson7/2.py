a, b, c = [int(i) for i in input().split()]

if a == b or a == c or b == c:
    Type = "Равнобедренный"
elif a == b == c:
    Type = "Равносторонний"
else:
    Type = "Разносторонний"
print(Type)
