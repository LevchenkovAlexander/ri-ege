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
        print("На ноль делить нельзя")
        result = "error"
    else:
        result = f / s

print(f, operator, s, "=", result)
