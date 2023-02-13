from string import ascii_lowercase as alf

s = input()
a = {}

for i in alf:
    a[i] = s.count(i)

for i in alf:
    print(f'{i} - {a.get(i)}')
