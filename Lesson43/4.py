d = [[0 for j in range(400)] for i in range(6)]

d[0][3] = 1

for i in range(4, 301):
    d[0][i] = d[0][i-1]
    for j in range(1, 6):
        d[j][i] = d[j][i-1] + (d[j-1][i//3] if i % 3 == 0 else 0) + (d[j-1][i//4] if i % 4 == 0 else 0)
        
print(d[5][300] + d[4][300] + d[3][300] + d[2][300] + d[1][300] + d[0][300])
