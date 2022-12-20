s = input()
sym = input()

cnt = 1
max_cnt = 0
for i in range(1, len(s)):
    if s[i] == s[i-1] == sym:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)
