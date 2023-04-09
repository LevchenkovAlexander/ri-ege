def game(x, i, win, p = -1):
    if i > max(win) or x >= 43:
        return i in win
    moves = [
        game(x + 1, i + 1, win, 0),
        game(x + 2, i + 1, win, 1),
        game(x * 2, i + 1, win, 2)
    ]
    
    if i != 0: moves.pop(p)
    
    return (all if i % 2 == win[0] % 2 else any)(moves)


print(f'19: {[s for s in range(1, 43) if game(s, 0, [2])]}')
print(f'20: {min(m := [s for s in range(1, 43) if game(s, 0, [3])]), max(m)}')
print(f'21: {[s for s in range(1, 43) if game(s, 0, [2, 4]) and not game(s, 0, [2])]}')