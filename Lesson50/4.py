def moves(game, x, i):
    return [game(x // 3, i + 1), game(x - 10, i + 1)]


def game_19(x, i):
    if x <= 10 or i > 2:
        return i == 2
    return any(moves(game_19, x, i))


def game_20(x, i):
    if x <= 10 or i > 3:
        return i == 3
    return (all if i % 2 else any)(moves(game_20, x, i))


def game_21(x, i):
    if x <= 10 or i > 4:
        return i == 4 or i == 2
    return (all if i % 2 == 0 else any)(moves(game_21, x, i))



def game_21_1(x, i):
    if x <= 10 or i > 2:
        return i == 2
    return (all if i % 2 == 0 else any)(moves(game_21_1, x, i))


ans_19 = []
ans_20 = []
ans_21 = []
for s in range(11, 1000):
    if game_19(s, 0):
        ans_19.append(s)
    if game_20(s, 0):
        ans_20.append(s)
    if game_21(s, 0) and not game_21_1(s, 0):
        ans_21.append(s)

print(f'19: {max(ans_19)}', f'20: {min(ans_20)} {max(ans_20)}', f'21: {len(ans_21)}', sep= "\n")