def unique(x):
    return x > 99 and x < 1000 and x % 10 == 5


a = [int(i) for i in open('Lesson34/'+input()+'.txt').read().splitlines()]
p = []

for i in range(len(a) - 2):
    if not unique(a[i]) and unique(a[i + 1]) and not unique(a[i + 2]):
        p.append(a[i] + a[i + 1] + a[i + 2])
print(len(p), max(p))
