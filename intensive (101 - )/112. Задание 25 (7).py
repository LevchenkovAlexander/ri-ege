def to_svn(num):
    s = ""
    while num:
        s = str(num % 7) + s
        num //= 7
    return s


from itertools import product

for q in range(10):
    for i in range(5):
        p = [''.join(i) for i in product("0123456789", repeat= i)]
        for s in p:
            num = int(f'1{s}586{q}6')
            f = to_svn(num)
            if f == f[::-1]:
                print(num, sum( [int(i) for i in f] ))