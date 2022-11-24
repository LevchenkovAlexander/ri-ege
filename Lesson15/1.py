k = 0


for i in range(10, 1001):
    n = bin(i)[2:]
    n = n.removeprefix('1')
    for j in range(len(n)-1-1):
        n = n.removeprefix('0')
    n = int(n, 2)
    new = i - n
    print(new)

