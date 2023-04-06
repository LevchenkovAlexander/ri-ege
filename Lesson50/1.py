def game(x, i, win_i):
    if x >= 33 or i > max(win_i):
        return i in win_i
    return (all if win_i[0] % 2 == i % 2 else any)([game(x + 3, i + 1, win_i), game(x * 2, i + 1, win_i)])


count = 0
for s in range(1, 33):
    if game(s, 0, [3]):
        count += 1
    if game(s, 0, [2, 4]) and not game(s, 0, [2]):
        print("21:", s)
print("20: ", count)