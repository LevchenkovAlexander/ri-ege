def f(x, y, cnt_pl, cnt_ml):
    if x == y and cnt_pl < cnt_ml:
        return 1
    if x >= y:
        return 0
    
    return f(x + 1, y, cnt_pl+1, cnt_ml) + f(x * 2, y, cnt_pl, cnt_ml + 1) + f(x * 3, y, cnt_pl, cnt_ml + 1)


print(f(1, 157, 0, 0))