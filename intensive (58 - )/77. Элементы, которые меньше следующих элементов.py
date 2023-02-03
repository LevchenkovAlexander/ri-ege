file = open('files\\77 intensive.txt')
f = list(map(int, file))
file.close()

cnt = 0

for i in range(len(f) - 1):
    if f[i] < f[i + 1]:
        cnt += 1
print(cnt)
