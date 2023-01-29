for x in '012345678':
    for y in '012345678':
        a = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
        if a % 170 == 0:
            print(a // 170)
            break