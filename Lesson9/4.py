from math import sqrt

a = float(input())
b = float(input())
c = float(input())

if (b**2 - 4*a*c) > 0:
    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - sqrt(b**2 - 4*a*c))/2*a
    print(x1, x2)

elif (b**2 - 4*a*c) == 0:
    x1 = (-b + sqrt(b**2 - 4*a*c))/2*a
    print(x1)
else:
    print("Нет корней")


