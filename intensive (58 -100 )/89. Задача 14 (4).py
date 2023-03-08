from string import ascii_lowercase as alf
for x in '0123456789'+alf[:12]:
    for y in '0123456789ab':
        f = int(f'{x}23{x}5', 22) - int(f'67{y}9{y}', 13)
        if f % 57 == 0:
            print(f//57)
            break