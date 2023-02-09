def check(x, y):
    return x % 2 == 0 and x % 4 == 0 and y % 2 and y % 11 == 0


a = [int(i) for i in open('Lesson34/'+input()+'.txt').read().splitlines()]
p = []

for i in range(len(a) - 1):
    if check(abs(a[i]), abs(a[i + 1])) or check(abs(a[i + 1]), abs(a[i])):
        p.append(a[i] + a[i + 1])
print(len(p), max(p))