def good(x, y):
    cnt = 0
    for i in range(4):
        if str(x)[i] == str(y)[i]:
            cnt += 1
    return cnt == 1

file = open("files\\90.txt")
a = list(map(int, file))
b = a.copy()
max_sum = max(b)
b.remove(max(b))
max_sum += max(b)
p = []
for i in range(len(a) - 2):
    if (good(a[i], a[i+1]) or good(a[i], a[i+2]) or good(a[i+1], a[i+2])) and sum(a[i:i+3]) < max_sum:
        p.append(sum(a[i:i+3]))
print(len(p), min(p))