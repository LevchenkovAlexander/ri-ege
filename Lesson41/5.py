from sys import setrecursionlimit
setrecursionlimit(3517)

def F(n):
    if n == 1:
        return 1
    return (2*n - 1) * F(n-1)
    
    
print(F(3516) / F(3513))