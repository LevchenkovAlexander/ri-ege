from string import ascii_uppercase as alf


def count_pairs(s):
    pair_count = 0
    for i in range(len(s)-1):
        if alf.find(s[i]) < alf.find(s[i+1]):
            pair_count += 1
    return pair_count

a = [i for i in open("files\\87.txt").read().splitlines()]
count ={}
for i in a:
    count[count_pairs(i)] = i
max_pairs = count[max(count.keys())]

l_cnt = [0 for i in alf]
for i in max_pairs:
    l_cnt[alf.index(i)] += 1

print(alf[l_cnt.index(min(l_cnt))])