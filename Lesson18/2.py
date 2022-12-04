s = input()
alf = "0123456789"
output = "Цифр нет"

for sym in s:
    for num in alf:
        if sym == num:
            output = "Цифра"
            break
print(output)
