def game(x, i, win_i):
    if x >= 33 or i > max(win_i):
        return i in win_i
    return (all if win_i[0] % 2 == i % 2 else any)([game(x + 3, i + 1, win_i), game(x * 2, i + 1, win_i)])


print(f'19: {min([s for s in range(1, 33) if game(s, 0, [2])])}')
print(f'20: {len([s for s in range(1, 33) if game(s, 0, [3])])}')
print(f'21: {(m := [s for s in range(1, 33) if game(s, 0, [2, 4]) and not game(s, 0, [2])])[-2], m[-1]}')