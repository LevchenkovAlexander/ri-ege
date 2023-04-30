def get_key(dict, value):
    for key in dict:
        if dict[key] == value: return key

data = sorted([[int(j) for j in i.split()] for i in open(f"Lesson57/{input()}.txt").read().splitlines()[1:]], key= lambda n: n[0])
dots = dict()

for i in data:
    if i[0] in dots:
        dots[i[0]].append(i[1])
    else:
        dots[i[0]] = [i[1]]

for row in dots:
    mx_ln, curr_ln = 1, 1
    _sorted = sorted(dots[row], reverse= True)
    for pos in range(len(_sorted)-1):
        if _sorted[pos] - _sorted[pos+1] == 1:
            curr_ln += 1
            mx_ln = max(mx_ln, curr_ln)
    dots[row] = mx_ln
    
print(f := max(dots.values()), get_key(dots, f))