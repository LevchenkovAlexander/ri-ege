s = input()
# print(s.count(" ") + 1)

count = 1

for sym in s:
    if sym == " ":
        count += 1

print(count)
