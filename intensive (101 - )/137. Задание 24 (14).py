s = open("files/137.txt").read()

s_zxy = s.replace("ZXY", "0")
s_zyx = s.replace("ZYX", "0")

d = [[0 for j in s] for i in range(2)]

for i in range(len(s_zxy)):
    if s_zxy[i] == "0":
        d[0][i] = d[0][i-1] + 1
for i in range(len(s_zyx)):
    if s_zyx[i] == "0":
        d[1][i] = d[1][i-1] + 1

print(max(max(d[0]), max(d[1])))