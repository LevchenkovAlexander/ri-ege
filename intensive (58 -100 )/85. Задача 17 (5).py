def check(x):
    return (x % 5 == x % 3) and (x % 31 == 0 or x % 47 == 0 or x % 53 == 0)
    


file = open("files\\85.txt")
a = list(map(int, file))

p = [ i for i in a if check(i) ]

print(len(p), min(p))
