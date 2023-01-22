n = int(input())
a = [int(input()) for i in range(n)]

negative = [i for i in a if i < 0]
zero = [i for i in a if i == 0]
positive = [i for i in a if i > 0]

print(*negative, *zero, *positive, sep= "\n")