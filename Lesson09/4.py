a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c
d = D**0.5

if D > 0:
    x1 = (-b + d)/2*a
    x2 = (-b - d)/2*a
    print(x1, x2)

elif D == 0:
    x1 = -b/2*a
    print(x1)
else:
    print("Нет корней")
