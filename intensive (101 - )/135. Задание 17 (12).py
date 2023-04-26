def chk(x, y):
    return "4" not in str(x) and "4" not in str(y)


data = [int(i) for i in open("files/135.txt").read().splitlines()]

avg = sum(data) / len(data)
ans = []

for i in range(len(data)-1):
    if (data[i] < avg or data[i+1] < avg) and chk(data[i], data[i+1]):
        ans.append(data[i] + data[i+1])
print(len(ans), min(ans))