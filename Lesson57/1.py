data = sorted([[int(j) for j in i.split()] for i in open(f"Lesson57/{input()}.txt").read().splitlines()[1:]], key= lambda n: n[0])
garden = dict()
mx_row, mn_tree = 0, 0
k = int(input())
for i in data:
    if i[0] in garden:
        garden[i[0]].append(i[1])
    else:
        garden[i[0]] = [i[1]]


for row in garden:
    trees = sorted(garden[row], reverse= True)
    for i in range(len(trees)-1):
        if trees[i] - trees[i+1] == k+1:
            mx_row, mn_tree = row, trees[i+1]+1

print(mx_row, mn_tree)