output = ""
for i in range(10):
    num = int(input())
    if num % 2 != 0:
        output = "NO"
        # break
        # здесь можно поставить брейк-поинт, чтобы программа дальше
        # не считывала числа, все равно результат будет "NO" после первого
        # введенного нечетного числа
    else:
        output = "YES"
print(output)
