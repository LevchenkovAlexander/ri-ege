from turtle import *

speed(100)
color("black", "red")
m = 30

begin_fill()
forward(9*m)
right(90)
for i in range(2):
    forward(3*m)
    right(90)
    forward(3*m)
    right(270)
for i in range(2):
    forward(3*m)
    right(90)
forward(9*m)
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