def moves(func, x, y, i, win):
    return [
        func(x + 1, y, i + 1, win),
        func(x, y + 1, i + 1, win),
        func(x * 2, y, i + 1, win),
        func(x, y * 2, i + 1, win),

    ]


def min_max(arr):
    return [min(arr), max(arr)]


def game(x, y, i, win):
    if x + y >= 91 or i > max(win):
        if x + y <= 110:
            return i in win
        else:
            return (i + 1) in win
    return (all if i % 2 == win[0] % 2 else any)(moves(game, x, y, i, win))


print(f'19: {min([s for s in range(1, 51) if game(40, s, 0, [2])])}')
print(f'20: {len([s for s in range(1, 51) if game(40, s, 0, [3])])}')
print(f'21: {min_max([s for s in range(1, 51) if game(40, s, 0, [2, 4]) and not game(40, s, 0, [2])])}')