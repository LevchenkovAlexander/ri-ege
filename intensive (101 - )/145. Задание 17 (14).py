a = list(map(int, open("files/145.txt")))

mx = max([i for i in a if i % 127 == 0])
count = 0
mn_sum = float("inf")

for i in range(len(a)-1):
    if (a[i] > mx or a[i+1] > mx) or ("31" in oct(a[i])[2:] or "31" in oct(a[i+1])[2:]):
        count += 1
        mn_sum = min(mn_sum, a[i] + a[i+1])
print(count, mn_sum)