a = 0
flag = True
while flag:
    for x in '0123456789abcd':
        m = int(f'8{x}12{x}', 14)
        n = int(f'8{x}542', 14)
        if m + a == n:
            print(a)
            flag = False
            break
    a += 1