n = int(input())

p = [int(input()) for i in range(n)]
cnt = 0
for i in range(len(p) - 1):
    if ((p[i] % 7 == 0) ^ (p[i + 1] % 7 == 0)) and p[i] % 2 != p[i + 1] % 2:
        cnt += 1
print(cnt)

