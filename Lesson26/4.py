def alg(s):
    while "1111" in s:
        s = s.replace("1111", "22", 1).replace("222", "1", 1)
    return s
        

a = []
b = list()
for i in range(200, 1000):
    f = alg("1" * i)
    a.append(f.count("1"))
    b.append(f)
print(b)
print(max(a), a.index(max(a)))
