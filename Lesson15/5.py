k = 0

for i in range(1000, 10000):
    n = str(i)
    if ((int(n[0]) + int(n[1]) == 4) and (int(n[2]) + int(n[3]) == 14) or
        (int(n[0]) + int(n[1]) == 14) and (int(n[2]) + int(n[3]) == 4)) and \
            (int(n[0]) % 2 != 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 != 0):
        k += 1

print(k)
