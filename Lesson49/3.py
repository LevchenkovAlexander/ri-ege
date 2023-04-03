def game(x, i, win_i):
    if x >= 25 or i > max(win_i):
        return i in win_i
    return (all if i % 2 == win_i[0] % 2 else any)([game(x + 2, i + 1, win_i), game(x * 2, i + 1, win_i)])


for s in range(1, 24):
    if game(s, 0, [3]):
        print("20:", s)
    if game(s, 0, [2, 4]) and not game(s, 0, [2]):
        print("21:", s)