file = open(f"Lesson58/{input()}.txt")
n, m = [int(i) for i in file.readline().split()]
cargos = sorted([int(i) for i in file.read().splitlines()])
truck = []

for cargo in cargos:
    if 205 <= cargo <= 210:
        truck.append(cargo)
        cargos.remove(cargo)
    elif cargo > 205:
        break
    
for i in cargos:
    if sum(truck) + i <= m:
        truck.append(i)
    else:
        break

for i in range(len(cargos)-1, -1, -1):
    for j in range(len(truck)):
        tmp = truck.copy()
        tmp.remove(truck[j])
        if cargos[i] > truck[j] and sum(tmp) + cargos[i] <= m:
            truck[j] = cargos[i]

print(len(truck), sum(truck))