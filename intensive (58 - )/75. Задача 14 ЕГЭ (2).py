for x in '0123456789a':
    for y in '0123456789a':
        a = int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)
        if a % 305 == 0:
            ans = a//305
            print(a)
            break