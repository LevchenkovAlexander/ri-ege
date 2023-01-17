a = [int(input()) for i in range(int(input()))]

cnt = 0
sums = []

for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        cnt += 1
        sums.append(a[i] + a[i + 1])
print(cnt, max(sums))