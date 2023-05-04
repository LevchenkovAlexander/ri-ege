file = open(f"Lesson58/{input()}.txt")
n, m = [int(i) for i in file.readline().split()]
data = sorted([[int(j) for j in (i.split())[:-1]] + [i.split()[-1]] for i in file.read().splitlines()], key= lambda n: (n[2], n[0]), reverse= True)

while data[-1][-1] == "A":
    m -= int((f := data.pop())[0]) * int(f[1])
count = 0
for i in range(len(data)-1, -1, -1):
    while m - int(data[i][0]) >= 0 and int(data[i][1]) > 0:
        m -= int(data[i][0])
        data[i][1] = int(int(data[i][1])-1)
        count += 1

print(count, m)