def func(data, id):
    if id == 0:
        return 0
    else:
        return data[id]['time'] + max([func(data, i) for i in data[id]["subs"]])


data = [[j for j in i.split("\t")[:-1]] for i in open("Lesson52/1.txt").read().splitlines()[1:]]
data = {int(i[0]): {"time" : int(i[1]), "subs" : [int(j) for j in i[2].split("; ")]} for i in data}

mx = 0
for i in data:
    mx = max(mx, func(data, i))
    
print(mx)