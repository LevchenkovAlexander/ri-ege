a = int("101101", 2)
r = range(2)

num = []
div = []

for i1 in r:
    for i2 in r:
        for i3 in r:
            for i4 in r:
                for i5 in r:
                    for i6 in r:
                        f = int(f'1{i1}1{i2}1{i3}1{i4}1{i5}{i6}1', 2)
                        if f % a == 0:
                            num.append(f)
                            div.append(f // a)              

for i in range(len(num)-1, -1, -1):
    print(num[i], div[i])