data = [[int(j) for j in i.split()] for i in open(f"Lesson57/{input()}.txt").read().splitlines()]
n, k = (f := data.pop(0))[0], f[1]
_data = dict()

for i in data:
    if i[0] in _data:
        _data[i[0]].append(i[1])
    else:  
        _data[i[0]] = [i[1]]

stores = {i: [] for i in _data}

for i in _data:
    for j in range(1, max(_data[i])+2):
        stores[i].append(0)
        if j in _data[i]:
            stores[i].pop()
            stores[i].append(j)
ans = []
for floor in stores:
    for i in range(len(stores[floor])-4):
        shops = stores[floor][i:i+4]
        if shops.count(0) == 1:
            f = shops.index(0)
            curr_ans = [floor, shops[f+1]-1 if f == 0 else shops[f-1]+1]
            if curr_ans not in ans:
                ans.append(curr_ans)
print(len(ans), ans[-1][0])