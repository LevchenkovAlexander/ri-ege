from turtle import *

speed(100)
color("black", "red")
m = 30

begin_fill()
for i in range(10):
    forward(9*m)
    right(90)
    forward(2*m)
    right(90)
end_fill()
canvas = getcanvas()
r = range(-100*m, 100*m, m)
cnt = 0
for x in r:
    for y in r:
        s = canvas.find_overlapping(x, y, x, y)
        if len(s):
            cnt += 1
print(cnt)
done()