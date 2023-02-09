k = 0

for x in range(1, 777):
    for y in range(1, 777):
        if (12 * x + 13 * y) == 777:
            k += 1
            print(f"{k} : ({x}; {y})")

print("количество -", k)
