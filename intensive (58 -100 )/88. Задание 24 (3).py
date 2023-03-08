a = open("files\\88.txt").read()
count = 0
ind = 0

for i in range(len(a) - 2):
    if a[i] <= a[i+1] <= a[i+2]:
        count += 1
        ind = i
    
    
print(count, ind)