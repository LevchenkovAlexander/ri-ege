data = [int(i) for i in open("files/139.txt").read().splitlines()[1:]]

count = 0
mx = float("-inf")

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] % 2 and data[j] % 2 and (avg := ((data[i] + data[j]) // 2)) in data:
            count += 1
            mx = max(mx, avg)
print(count, mx)