def dels(num):
    dels = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            dels.add(i)
            dels.add(num//i)
    return dels


max_num = float('-inf')
max_count = 0
for i in range(120115, 120200 + 1):
    d = dels(i)
    
    if max_count <= len(d):
        max_count = len(d)
        max_num = i

print(max_count, max_num)    