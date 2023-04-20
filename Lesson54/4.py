from turtle import *

color("black", "red")
speed(100)
m = 30

begin_fill()
left(30)
for i in range(15):
    for j in range(2):
        forward(5*m)
        left(60)
    forward(5*m)
    left(120)
    forward(10*m)
    left(120)
end_fill()

canvas = getcanvas()
r = range(-100*m, 100*m, m)
cnt = 0

for x in r:
    for y in r:
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5:
            cnt += 1
print(cnt)
done()