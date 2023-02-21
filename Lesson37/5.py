def f(s):
    return "A" in s and "B" in s and "C" in s


a = open("Lesson37\\5.txt").read()
s = ''
count = 0
for i in range(len(a)-1):
    s += a[i]
    if f(s+a[i+1]):
        if len(s) > 2:    
            count += 1
            s = ""
        else: s = a[i]
    elif i == len(a) - 2 and len(s) > 1: count += 1

            
                                
print(count)