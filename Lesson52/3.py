def func(data, id):
    if id == 0:
        return 0
    else:
        return data[id]['time'] + max([func(data, i) for i in data[id]["subs"]])


data = [[j for j in i.split("\t")] for i in open("Lesson52/3.txt").read().splitlines()[1:]]
data = {int(i[0]): {"time" : int(i[1]), "subs" : [int(j) for j in i[2].split(";")]} for i in data}


time_1 = time_2 = 0
for i in data:
    time_1 = max(time_1, data[i]["time"])
    time_2 = max(time_2, func(data, i))
    
print(time_2 - time_1)