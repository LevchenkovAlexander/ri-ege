r = range(2)
print("x y w z")

for x in r:
    for y in r:
        for w in r:
            for z in r:
                if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                    print(x, y, w, z)