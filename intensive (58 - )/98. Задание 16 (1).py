def fibonachchi(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return fibonachchi(n-2) + fibonachchi(n-1)


print(fibonachchi(19))