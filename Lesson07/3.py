f = int(input())
s = int(input())

operator = input()

if operator == "+":
    result = f + s
elif operator == "-":
    result = f - s
elif operator == "*":
    result = f * s
elif operator == "/":
    if s == 0:
        result = "На ноль делить нельзя!"
    else:
        result = f / s
else: 
    result = "Неверный оператор"

print(result)
