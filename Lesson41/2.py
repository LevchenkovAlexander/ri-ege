def F(n):
    if n < 3:
        return n + 3
    if n >= 3 and n % 3 == 0:
        return (n+2) * F(n-4)
    if n >= 3 and n % 3:
        return n + F(n-1) + 2* F(n-2)
    
print(F(20))