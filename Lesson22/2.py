s = input()

max_count = 0
max_sym = ""

for i, sym in enumerate(s):
    if s.count(sym) >= max_count:
        max_count = s.count(sym)
        max_sym = sym
print(max_sym)
