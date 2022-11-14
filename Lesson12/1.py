n = int(input())

s = 0
j = -1
k = 1


for i in range(n):
    s = k+j
    j = k
    k = s
    print(s, end=' ')



