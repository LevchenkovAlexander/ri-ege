file = open(f'Lesson62/{input()}.txt')
data = [int(i) for i in file.read().splitlines()]
n = data.pop(0)

mn_cost = float("inf")
p = None
for i in range(n):
    cost = 0
    for j in range(n):
        cost += data[j] * min(abs(j - i), n - abs(j - i))
    if cost < mn_cost:
        mn_cost = cost
        p = i + 1
        
print(p)