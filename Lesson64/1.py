a = [[int(j) for j in i.split()] for i in open(f"Lesson64/{input()}.txt").read().splitlines()]
n = a.pop(0)[0]
k = 5
d = [[i for i in range(n)] for j in range(k)]

d[max(a[0]) % 5][0] = max(a[0])

for i in range(1, n):
    for j in range(k):
        d[j][i] = max([d[p][i-1] + max([el if (el % k == (j-p) % k) else 0 for el in a[i]]) for p in range(k)])    

print(max([d[j][-1] for j in range(1, k)]))