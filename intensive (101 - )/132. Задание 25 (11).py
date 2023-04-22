ans = []

for x1 in range(8):
    for x2 in range(8):
        if (f := int(f'1{x1}345{x2}700', 8)) % (d := int("114", 8)) == 0:
            ans.append([f, f//d])
print(*ans[::-1], sep= "\n")