s = open("Lesson36\\1.txt").read()

d = [1 if i == 'X' else 0 for i in s ]

for i in range(1, len(s)):
    if s[i] == "X": d[i] = d[i - 1] + 1

print(max(d))