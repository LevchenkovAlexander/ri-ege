from itertools import product

prod = [''.join(i) for i in product("апрсу", repeat= 4)]

for i, p in enumerate(prod):
    print(i + 1, p)
    if "а" not in p:
        print(i + 1, p)
        break
