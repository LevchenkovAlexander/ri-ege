s = open("files/141.txt").read()
count = 0

for i in range(len(s)):
    if s[i] == "(":
        count += 1
    if count == 10000:
        print(i + 1)
        break