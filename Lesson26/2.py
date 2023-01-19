def alg(s):
    print(s)
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">3" in s:
            s = s.replace(">3","1>", 1)
    print(s)
    return [int(i) for i in s if i != ">"]


f = ">" + "3"*30 + "1"*10 + "2"*20 
print(sum(alg(f)))
print(alg(f))
