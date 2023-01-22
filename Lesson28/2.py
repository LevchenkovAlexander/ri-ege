n = int(input())

a = [int(input()) for i in range(n)]
a.remove(max(a))
a.remove(min(a))
print(*a, sep= "\n")
