s = open("Lesson36\\4.txt").read()

d = [1 for i in s]

for i in range(1, len(s)):
    if s[i-1]+s[i] != "PP": d[i] = d[i-1] + 1

print(max(d))