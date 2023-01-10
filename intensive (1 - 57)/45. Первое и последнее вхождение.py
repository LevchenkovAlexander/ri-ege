s = input()
q = input()

tmp = []

for i, sym in enumerate(s):
    if sym == q:
        tmp.append(i)
if len(tmp) > 0:
    print(f"Номер первого вхождения символа \"{q}\" в строку \"{s}\" - {min(tmp)}")
    print(f"Номер последнего вхождения символа \"{q}\" в строку \"{s}\" - {max(tmp)}")
else:
    print(f"Символа \"{q}\" в строке \"{s}\" нет")

