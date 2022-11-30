b = 10
k = 5
t = 0.5

for i in range(100):
    for j in range(100):
        for f in range(100):
            if (i*b + j*k + f*t) == 100 and (i + j + f) == 100:
                print(f"{i} быков, {j} коров, {f} телят")

