s = open("Lesson36\\3.txt").read()

d = [1 if i == 'L' else float('-inf') for i in s]

for i in range(1, len(s)):
    if (s[i-1] + s[i]) in "LDR": d[i] = max(d[i-1], 1) + 1
    if s[i - 1] == "R" and s[i] == "L" and d[i-1] != float('-inf'): d[i] = d[i-1] + 1

print(max(d))