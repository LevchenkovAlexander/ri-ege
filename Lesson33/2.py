f = [int(i) for i in open(f'{input()}.txt').read().splitlines()]

avg_m = [i for i in f if i % 2 == 0]
avg = sum(avg_m)/len(avg_m)

pairs = []

for i in range(len(f) - 1):
    if (f[i] % 3 == 0 and f[i + 1] < avg) or (f[i + 1] % 3 == 0 and f[i] < avg):
        pairs.append(f[i] + f[i + 1])
print(len(pairs), max(pairs))