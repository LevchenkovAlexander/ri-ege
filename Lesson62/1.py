file = open(f'Lesson62/{input()}.txt')
data = [int(i) for i in file.read().splitlines()]
n = data.pop(0)
mx_sm = mn_ln = float("-inf")
for i in range(n):
    sm = 0
    ln = 0
    for j in range(i, n):
        sm += data[j]
        ln += 1
        if sm % 89 == 0:
            if sm > mx_sm:
                mx_sm = sm
                mn_ln = ln
            if sm == mx_sm:
                mn_ln = min(ln, mn_ln)
print(mn_ln)