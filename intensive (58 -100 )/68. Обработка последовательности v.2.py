n = int(input())

a = [int(input()) for i in range(n)]
cnt = 0
max_sum = float('-inf')
for ind, i in enumerate(a):
    for j in a[ind + 1:]:
        if i % 3 == 0 or j % 3 == 0:
            cnt += 1
            if max_sum < i + j:
                max_sum = i + j
print(cnt, max_sum)
        
        
