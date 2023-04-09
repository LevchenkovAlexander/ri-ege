def game(x, y, z, i, win, func = all):
    if x + y + z >= 73 or i > max(win):
        return i in win
    moves = [
        game(x + 3, y, z, i + 1, win, func),
        game(x + 13, y, z, i + 1, win, func),
        game(x + 23, y, z, i + 1, win, func),
        game(x, y + 3, z, i + 1, win, func),
        game(x, y + 13, z, i + 1, win, func),
        game(x, y + 23, z, i + 1, win, func),
        game(x, y, z + 3, i + 1, win, func),
        game(x, y, z + 13, i + 1, win, func),
        game(x, y, z + 23, i + 1, win, func)
        ]
    
    return (func if i % 2 == win[0] % 2 else any)(moves)


print(f'19: {min([s for s in range(1, 24) if game(2, s, 2*s, 0, [2], any)])}')
print(f'20: {min(arr := [s for s in range(1, 24) if game(2, s, 2*s, 0, [3])]), max(arr)}')
print(f'21: {[s for s in range(1, 24) if game(2, s, 2*s, 0, [2, 4]) and not(game(2, s, 2*s, 0, [2]) or game(2, s, 2*s, 0, [4])) and not game(2, s, 2*s, 0, [3])]}')

