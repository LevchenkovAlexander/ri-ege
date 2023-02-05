f = [int(i) for i in open(f'{input()}.txt').read().splitlines()]

cnt = 0
max_ = float('-inf')

for i in range(len(f) - 1):
    if f[i] * f[i + 1] % 15 == 0 and (f[i] + f[i + 1]) % 7 == 0:
        cnt += 1
        max_ = max(max_, f[i] + f[i + 1])
        
print(cnt, max_)
