s = input()
cnt = 0

for sym in s:
    if sym == sym.lower():
        cnt += 1
print(cnt)
