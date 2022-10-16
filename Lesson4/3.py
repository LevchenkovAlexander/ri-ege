#Я не уверен, что имеется ввиду под тем, что все числа вводятся на одной строке

T = int(input())
t = int(input())
humidity = int(input())

if (humidity < 80) & (t > T):
    print("on")
else:
    print("off")

