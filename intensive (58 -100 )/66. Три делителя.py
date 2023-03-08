n = int(input())

ans = []
for i in range(1, n + 1):
    del_st = []
    del_end = []
    dels = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            del_st.append(j)
            del_end.append(i // j)
            
    dels = list(set(del_st + del_end[::-1]))
    
    if len(dels) == 3:
        ans.append(f" { i } - { dels }  ")
        
for i in ans:
    print(i, "\n")