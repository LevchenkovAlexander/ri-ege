f = [int(i) for i in open(f'{input()}.txt').read().splitlines()]

pairs = []

for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if ((f[i] + f[j]) % 60 == 0) and (f[i] % 40 == 0 or f[j] % 40 == 0):
            pairs.append(f[i] + f[j])
print(len(pairs), max(pairs))