def func(t):
    s = [sum([int(i) for i in str(j)]) for j in t]
    for i in s:
        if i in t:
            return True
    return False

a = [int(i) for i in open('17.7.txt').read().splitlines()]
sum50_arr = [i for i in a if i % 50 == 0]
sum50 = sum([ sum([int(i) for i in str(x)]) for x in sum50_arr ])
p = []

for i in range(len(a) - 2):
    tr = a[i:i+3]
    if func(tr) and sum(tr) < sum50:
        p.append(sum(tr))
print(len(p), max(p))        
