file = open("files/144.txt")
s = int(file.readline().split()[0])
data = [int(i) for i in file.read().splitlines()]
data.sort(reverse= True)
disk = []

while sum(disk) + data[-1] <= s:
    disk.append(data.pop())
    
while sum(disk[:-1]) + data[-1] <= s:
    disk.pop()
    disk.append(data.pop())
    
print(len(disk), disk[-1])