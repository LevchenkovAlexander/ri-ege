from string import ascii_uppercase as alf
a = open("Lesson37\\3.txt").read()
count = [0 for i in alf]
for i in range(1, len(a) - 1):
    if a[i-1] == "X" and a[i+1] == "Z":
        count[alf.index(a[i])] += 1
        
print(alf[count.index(max(count))], max(count), sep= "")