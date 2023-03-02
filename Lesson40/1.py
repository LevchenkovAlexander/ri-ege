def func(num):
    s = 1
    for i in str(num):
        if int(i) % 2:
            s *= int(i)
    return s


while 1: print(func(int(input())))