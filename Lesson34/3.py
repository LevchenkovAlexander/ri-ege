a = [int(i) for i in open('Lesson34\\'+input()+'.txt').read().splitlines()]
p = []

min103 = min( [i for i in a if i % 103 == 0] )

for i in range(len(a) - 1):
    sum_ = a[i] + a[i + 1]
    if sum_ % 2 == 0 and (a[i] - a[i + 1]) % min103 == 0:
        p.append(sum_)
        
print(len(p), max(p))
