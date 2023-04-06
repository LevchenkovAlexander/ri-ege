def moves(func, x, y, i):
    return [func(x + 1, y, i + 1), 
            func(x, y + 1, i + 1),
            func(x + y, y, i + 1),
            func(x, y + x, i + 1)]

def game_19(x, y, i):
    if i > 2 or x + y > 72:
        return i == 2
    return any(moves(game_19, x, y, i))
    
    
def game_20(x, y, i):
    if i > 3 or x + y > 72:
        return i == 3
    return (all if i % 2 else any)(moves(game_20, x, y, i))


def game_21(x, y, i):
    if i > 4 or x + y > 72:
        return i == 4 or i == 2
    return (all if i % 2 == 0 else any)(moves(game_21, x, y, i))


def game_21_1(x, y, i):
    if i > 2 or x + y > 72:
        return i == 2
    return (all if i % 2 == 0 else any)(moves(game_21_1, x, y, i))
    
    
ans_19 = []
ans_20 = []
ans_21 = []

for s in range(1, 63):
    if game_19(9, s, 0):
        ans_19.append(s)
    if game_20(9, s, 0):
        ans_20.append(s)
    if game_21(9, s, 0) and not game_21_1(9, s, 0):
        ans_21.append(s)

print("19:", min(ans_19))
print("20:", *ans_20)
print("21:", *ans_21)
