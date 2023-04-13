def f(num):
    return int((a := bin(num)[2:]).count("1") == 2 and a.count("0") > 0)
    

def check(tr):
    return f(tr[0]) + f(tr[1]) + f(tr[2]) >= 2
    

arr = list(map(int, open("files/124.txt")))
count = mx = 0

for i in range(len(arr) - 2):
    tr = arr[i:i+3]
    if check(tr):
        count += 1
        tr.remove(min(tr))
        mx = max(mx, sum(tr))
        
print(count, mx)