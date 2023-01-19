def alg(s):
    while "1111" in s:
        s = s.replace("1111", "22", 1).replace("222", "1", 1)
    return s


a = []
for i in range(201, 1000):
    f = alg("1" * i)
    a.append(f.count("1"))
print(max(a), 201 + a.index(max(a)))