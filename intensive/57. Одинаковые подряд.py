s = input()
cnt = 1
max_cnt = cnt
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt+=1 
    else:
        cnt = 1
    
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
