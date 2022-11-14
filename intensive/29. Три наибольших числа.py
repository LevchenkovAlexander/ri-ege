n = int(input())

m0 = float('-inf')
m1 = float('-inf')
m2 = float('-inf')

for i in range(n):
    x = int(input())
    if x > m2:
        if x > m1:
            if x > m0:
                m0 = x
            else:
                m1 = x
        else:
            m2 = x

print(m0, m1, m2)
