def game_19(x, y, i):
    if (x + y) >= 133 or i > 2:
        return i == 2
    return (any)([
        game_19(x + 1, y, i + 1),
        game_19(x, y + 1, i + 1),
        game_19(x * 4, y, i + 1),
        game_19(x, y * 4, i + 1)
    ])
    
    
def game_20(x, y, i):
    if (x + y) >= 133 or i > 3:
        return i == 3
    return (all if i % 2 else any)([
        game_20(x + 1, y, i + 1),
        game_20(x, y + 1, i + 1),
        game_20(x * 4, y, i + 1),
        game_20(x, y * 4, i + 1)
    ])
    
def game_21(x, y, i):
    if (x + y) >= 133 or i > 4:
        return i == 4 or i == 2
    return (all if i % 2 == 0 else any)([
        game_21(x + 1, y, i + 1),
        game_21(x, y + 1, i + 1),
        game_21(x * 4, y, i + 1),
        game_21(x, y * 4, i + 1)
    ])
 
def game_21_1(x, y, i):
    if (x + y) >= 133 or i > 2:
        return i == 2
    return (all if i % 2 == 0 else any)([
        game_21_1(x + 1, y, i + 1),
        game_21_1(x, y + 1, i + 1),
        game_21_1(x * 4, y, i + 1),
        game_21_1(x, y * 4, i + 1)
    ])
    
    
ans_19 = []
ans_20 = []
ans_21 = []

for s in range(1, 126):
    if game_19(7, s, 0):
        ans_19.append(s)
    if game_20(7, s, 0):
        ans_20.append(s)
    if game_21(7, s, 0) and not game_21_1(7, s, 0):
        ans_21.append(s)

print("19:", min(ans_19))
print("20:", *ans_20)
print("21:", *ans_21)
