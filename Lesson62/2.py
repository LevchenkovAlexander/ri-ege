file = open(f'Lesson62/{input()}.txt')
data = [int(i) for i in file.read().splitlines()]
n = data.pop(0)

mx_sm = float("-inf")
for i in range(n):
    k = 0
    sm = 0
    for j in range(i, n):
        sm += data[j]
        if abs(data[j]) % 2 == 0 and data[j] > 0:
            k += 1
        if k == 30:
            mx_sm = max(mx_sm, sm)
            
print(mx_sm)