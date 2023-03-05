def func(num):
    s = 1
    for i in str(num):
        if int(i) % 2:
            s *= int(i)
    print(s)