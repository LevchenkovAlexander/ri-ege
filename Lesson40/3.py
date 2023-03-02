def mid(n1, n2, n3):
    return (n1 + n2 + n3) - max(n1, n2, n3) - min(n1, n2, n3)


while 1: print(mid(int(input()), int(input()), int(input())))