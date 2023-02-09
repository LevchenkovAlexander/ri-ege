def f(x, y):
    return x > diff and y < diff


a = [int(i) for i in open('Lesson34\\'+input()+'.txt').read().splitlines()]
p = []

diff_m = [i for i in a if i % 100 == 52]
diff = max(diff_m) - min(diff_m)

for i in range(len(a) - 1):
    if (a[i] < diff) ^ (a[i + 1] < diff):
        p.append(a[i] + a[i+1])
        
print(len(p), max(p))
