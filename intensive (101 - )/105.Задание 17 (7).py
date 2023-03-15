file = open("files\\105.txt")
a = list(map(int, file))

avg = sum(a)/len(a)

cnt = 0
mx_sum = float('-inf')

for i in range(len(a) - 2):
    t = a[i:i+3]
    count = 0
    count2 = 0
    for j in t:
        if j > avg: count += 1
        if abs(j) % 11 == 0: count2 += 1
    if count >= 2 and count2 >= 1:
        cnt += 1
        mx_sum = max(mx_sum, sum(t))
print(cnt, mx_sum)