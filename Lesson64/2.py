a = [int(i) for i in open(f"Lesson64/{input()}.txt").read().splitlines()]
n = a.pop(0)
k = a.pop(0)

d = [float('-inf') for i in range(n)]
for i in range(1, n):
    d[i] = max(d[i-1], a[i-k])
    
print(max(d))