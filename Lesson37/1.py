a = [i for i in open("Lesson37\\1.txt").read().splitlines()]
count = 0
for i in a:
    if i.count("K") > i.count("U"): count += 1
print(count)