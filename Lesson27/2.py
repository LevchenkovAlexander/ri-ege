s = input()
a = [int(i) for i in s if i != " "]
a.sort()
print(a)
print(a[::-1])
