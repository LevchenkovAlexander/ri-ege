f = [int(i) for i in open(f'files\\{input()}.txt').read().splitlines()]

cnt = 0

for i in range(len(f) - 1):
    if f[i] < f[i + 1]:
        cnt += 1
print(cnt)
