def f(s):
    return "A" in s and "B" in s and "C" in s


a = open("Lesson37\\5.txt").read()
s = ''
count = 0
for i in range(len(a)):
    s += a[i]
    if f(s) or i == len(a) - 1:
        if len(s) > 3:    
            count += 1
        s = ''
print(count)