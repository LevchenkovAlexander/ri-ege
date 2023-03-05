def calc(str):                
    s = str.split()
    num1 = int(s[0])
    operator = s[1]
    num2 = int(s[2])
    if operator == "+": print(num1 + num2)
    elif operator == "-": print(num1 - num2)
    elif operator == "*": print(num1 * num2)
    elif operator == "^": print(num1 ** num2)
    elif operator == "/":
        if num2 == 0: print("Деление на 0")
        else: print(num1 / num2)
    else: print("Ошибка операции")