s = open("Lesson37\\5.txt").read()

a, b, c = 0, 0, 0
count = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] == "A": a += 1
        if s[j] == "B": b += 1
        if s[j] == "C": c += 1
        
        if a*b*c == 0:
            if j- i  >= 2:
                count += 1
        else:
            a, b, c = 0, 0, 0
            break
        
print(count)