file = open("Lesson55/3.txt")
s, n = (f := [int(i) for i in file.readline().split()])[0], f[1]
all = sorted([int(i) for i in file.read().splitlines()], reverse= True)
conts = []

while sum(conts) + all[-1] <= s:
    conts.append(all.pop())

while len(all) and sum(conts[:-1]) + all[-1] <= s:
    conts.pop()
    conts.append(all.pop())

print(len(conts), conts[-1])