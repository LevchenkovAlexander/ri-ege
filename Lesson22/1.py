s = input()
cnt = 0

for sym in s:
    if sym == sym.lower() and sym.isalpha():
        cnt += 1
print(cnt)
