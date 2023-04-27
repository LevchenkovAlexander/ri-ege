data = list(map(int, open("files/136.txt")))

avg = sum(data) / len(data)
ans = []

for i in range(len(data)-1):
    if data[i] > avg or data[i+1] > avg:
        ans.append(data[i] + data[i+1])
    
print(len(ans), max(ans))