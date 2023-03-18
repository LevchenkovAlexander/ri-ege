from string import ascii_uppercase as alf

a = [ i for i in open("files\\107.txt").read().splitlines() ]
count = 0

for j in a:
    for i in alf:
        if f"F{i}O" in j:
            count += 1
print(count)