a = [int(i) for i in open(f"Lesson63/{input()}.txt").read().splitlines()]
n = a.pop(0)
k = 89

d = {key: [[float("-inf") for i in a] for j in range(k)] for key in ["sum", "len"]}

d["sum"][a[0] % k][0] = a[0]
d["len"][a[0] % k][0] = 1
last_progress = 0
for i in range(1, n):
    progress = (i + 1) * 100 // n
    if progress != last_progress:
        print(progress, "%")
        last_progress = progress
    for j in range(k):
        if d["sum"][(j - a[i]) % k][i-1] != float("-inf"):
            d["sum"][j][i] = a[i] + d["sum"][(j - a[i]) % k][i-1]
            d["len"][j][i] = 1 + d["len"][(j - a[i] % k)][i-1]
        elif a[i] % k == j:
            d["sum"][j][i] = a[i]
            d["len"][j][i] = 1

max_sum = max(d["sum"][0])
min_len = min([d["len"][0][i] for i in range(len(d["len"][0])) if d["sum"][0][i] == max_sum])
print(min_len)