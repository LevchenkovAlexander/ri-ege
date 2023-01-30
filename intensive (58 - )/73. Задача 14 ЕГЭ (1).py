f = True
for x in '0123456789ab':
    if f:
        for y in '0123456789ab':
            a = int(f'{x}231{y}', 12) + int(f'78{x}98{y}', 14)
            if a % 99 == 0:
                print(a // 99)
                f = False
                break