def f(x):
    return abs(x) % 10 == 6 and abs(x) % 3 == 0


file = open('files/test.txt')
a = list(map(int, file))

p = []

for i in range(len(a) - 1):
    if f(a[i]) or f(a[i + 1]):
        p.append(min(a[i], a[i+1]))
print(len(p), min(p))
