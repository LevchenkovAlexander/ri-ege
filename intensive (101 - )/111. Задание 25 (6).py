from itertools import product

count = 0
i = 0

while count < 5:
    p = [''.join(j) for j in product("0123456789", repeat= i)]
    for n in p:    
        a = int(f'12345{n}76')
        if a % 73 == 0:
            print(a, a // 73)
            count += 1
        if count >= 5:
            break
    i += 1