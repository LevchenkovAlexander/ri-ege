a = open("Lesson37\\2.txt").read()
count = 0
len_i = 1
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        len_i += 1
    else:
        if len_i == 5:
            count += 1
        len_i = 1
print(count)