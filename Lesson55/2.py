a = [int(i) for i in open("Lesson55/2.txt").read().splitlines()]
n = a.pop(0)
a.sort(reverse= True)
boxes = [a[0]]

for i in a:
    if boxes[-1] - 17 >= i:
        boxes.append(i)

print(len(boxes), boxes[-1])