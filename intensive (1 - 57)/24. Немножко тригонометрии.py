from math import radians, sin, cos, tan

x = float(input())
x = radians(x)
y = sin(x) + cos(x) + tan(x)**2

print(y)
