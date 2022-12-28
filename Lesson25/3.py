from itertools import product

prod = [''.join(i) for i in product("аворт", repeat= 4)]

for i, p in enumerate(prod):
    if p == "вата":
        print(i + 1, p)
        break
