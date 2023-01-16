def alg(s):
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        elif ">2" in s:
            s = s.replace(">2", "2>", 1)
        else:
            s = s.replace(">3","1>", 1)
    return [int(i) for i in s]


f = "1"*10 + "2"*20 + "3"*30
print(sum(alg(f)))
