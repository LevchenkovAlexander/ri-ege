def check(tr):
    for i in tr:
        if "1" not in str(i):
            return 0
    return 1


a = list(map(int, open("files/116.txt")))

avg = sum(a) / len(a)
ans = []

for i in range(len(a) - 2):
    tr = a[i:i+3]
    if int(a[i] > avg) + int(a[i+1] > avg) + int(a[i + 2] > avg) >= 2 and check(tr):
        ans.append(sum(tr))
print(len(ans), max(ans))
    