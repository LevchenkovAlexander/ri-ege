r = range(2)
print("x y w z")

for x in r:
    for y in r:
        for w in r:
            for z in r:
                if (x or not z) and (x == (not w)) and (x <= y):
                    print(x, y, w, z)