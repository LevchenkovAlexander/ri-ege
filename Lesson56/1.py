file = open(f'Lesson56/{input()}.txt')
s, n = (f:=[int(i) for i in file.readline().split()])[0], f[1]
data = sorted([int(i) for i in file.read().splitlines()], reverse= True)

disk = []

while sum(disk) + data[-1] <= s:
    disk.append(data.pop())

while len(data) and sum(disk[:-1]) + data[-1] <= s:
    disk.pop()
    disk.append(data.pop())
    
print(len(disk), disk[-1])