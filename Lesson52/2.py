def func(data, id):
    if id == 0:
        return 0
    else:
        return data[id]['time'] + (3 if data[id]["subs"][0] != 0 else 0) + max([func(data, i) for i in data[id]["subs"]])


data = [[j for j in i.split("\t")[:-1]] for i in open("Lesson52/2.txt").read().splitlines()[1:]]
data = {int(i[0]): {"time" : int(i[1]), "subs" : [int(j) if len(j) else 0 for j in i[2].split(";")]} for i in data}

mx = count = 0
for i in data:
    if count < 48:
        mx = max(mx, func(data, i))
        count += 1
    else: break
    
print(mx)