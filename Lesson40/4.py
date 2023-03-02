def calc(num1, operator, num2): # правильные входные данные
# def calc(str):                # удобный ввод
#     s = str.split()
#     num1 = int(s[0])
#     operator = s[1]
#     num2 = int(s[2])
    if operator == "+": return num1 + num2
    elif operator == "-": return num1 - num2
    elif operator == "*": return num1 * num2
    elif operator == "^": return num1 ** num2
    elif operator == "/":
        if num2 == 0: return "Деление на 0"
        else: return num1 / num2 if num1 % num2 else num1 // num2
    else: return "Ошибка операции"
    

# тест первого варианта
# while 1: print(calc(int(input()), input(), int(input())))

# тест второго варианта
# while 1: print(calc(input()))