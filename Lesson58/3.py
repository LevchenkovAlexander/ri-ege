file = open(f"Lesson58/{input()}.txt")
n = int(file.readline())
data = sorted([[int(j) for j in i.split()] for i in file.read().splitlines()])
signals = {}
for i in data:
    if i[1] in signals:
        signals[i[1]]["values"].append(i[0])
        signals[i[1]]["len"] += 1
    else:
        signals[i[1]] = {"values": [i[0]], "len": 1}
        
mx = [float("-inf"), 0]
int_values = []

for i in signals:
    if signals[i]["len"] >= mx[0]:
        mx = [signals[i]["len"], i]
        int_values = set([int(str(i)[:-1]) if i >= 10 or i <= -10 else i for i in signals[i]["values"]])
    
print(mx[1], len(int_values))