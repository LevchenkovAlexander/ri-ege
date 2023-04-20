from turtle import *

speed(100)
color("black", "red")
m = 20

begin_fill()
for i in range(8):
    forward(6*m)
    right(120)
end_fill()

cnt = 0
canvas = getcanvas()
r = range(-100*m, 100*m, m)
# tracer(1000)

for x in r:
    for y in r:
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5:
            cnt += 1
        # penup()
        # goto(x, y)
        # dot()
print(cnt)
done()