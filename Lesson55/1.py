file = open("Lesson55/1.txt")

mx, n = (f := [int(i) for i in file.readline().split()])[0], f[1]
a = sorted([int(i) for i in file.read().splitlines()], reverse=True)

disk = []

while sum(disk) + a[-1] < mx:
    disk.append(a.pop())

while len(a) and sum(disk[:-1]) + a[-1] < mx:
    disk.pop()
    disk.append(a.pop()) 

print(len(disk), disk[-1])