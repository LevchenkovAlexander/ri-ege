a = open("Lesson37\\4.txt").read()
count = 0
max_count = float('-inf')

for i in range(1, len(a)):
    if a[i-1].isalpha() and a[i].isnumeric():
        count += 1
    elif a[i-1].isnumeric() and a[i].isalpha():
        continue
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)