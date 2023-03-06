def F(n):
    if n <= 13:
        return n*n*n + n*n+1
    if n > 13 and n % 3 == 0:
        return F(n-1) + 2*n*n - 3
    if n > 13 and n % 3:
        return F(n-2) + 3*n + 6
    

count = 0
for i in range(1, 1000 + 1):
    d = F(i)
    if len([j for j in str(d) if int(j) % 2 == 0]) == 0:
        count += 1

print(count)