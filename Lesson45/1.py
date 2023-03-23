r = range(2)
print("x y w z")

for x in r:
    for y in r:
        for w in r:
            for z in r:
                if (x or y) and not (y == z) and not w:
                    print(x, y, w, z)