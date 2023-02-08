file = open('files/78.txt')

a = list(map(int, file))
list_171 = [i for i in a if i % 171 == 0]
max_171 = max(list_171)
p = []


for i in range(len(a) - 1):
    if (a[i] < max_171 or a[i + 1] < max_171) and (a[i] % 2 or a[i + 1] % 2):
        p.append(a[i] + a[i + 1])
print(len(p), max(p))
 