def sum_even(x):
    return sum([int(i) for i in str(x) if int(i) % 2 == 0])


def sum_odd(x):
    return sum([int(i) for i in str(x) if int(i) % 2])


a = [int(i) for i in open(input() + ".txt").read().splitlines()]
min_a = min([ i for i in a if i % 2 == 0 ])
p = []

for i in range(len(a) - 1):
    if (sum_even(a[i]) > sum_odd(a[i])) and (sum_even(a[i + 1]) > sum_odd(a[i + 1])):
        if (a[i] + a[i + 1]) % min_a == 0:
            p.append(a[i] + a[i + 1])
print(len(p), max(p))
