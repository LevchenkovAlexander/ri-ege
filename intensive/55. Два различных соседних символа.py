s = input()
cnt = 1
max_cnt = cnt

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = cnt if cnt > max_cnt else max_cnt
print(max_cnt)
