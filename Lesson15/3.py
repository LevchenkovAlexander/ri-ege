for i in range(100000):
    n = bin(i)[2:]
    c0 = 0
    c1 = 0
    for j in range(len(n)):
        if (n[j] == "1") and ((j+1) % 2 == 0):
            c1 += 1
        elif (n[j] == "0") and ((j+1) % 2 != 0):
            c0 += 1
    if abs(c0 - c1) == 5:
        print(n)
        print(abs(c0 - c1))
        print(i)
        break

