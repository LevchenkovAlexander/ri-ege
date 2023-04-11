def f(num):
    return int((a := bin(num)[2:]).count("1") == 2 and a.count("0") > 0)
    

def check(tr):
    return f(tr[0]) + f(tr[1]) + f(tr[2]) >= 2
    

arr = list(map(int, open("files/124.txt")))
ans = []

for i in range(len(arr) - 2):
    tr = arr[i:i+3]
    if check(tr):
        ans.append(sum(tr))
        
print(len(ans), max(ans))