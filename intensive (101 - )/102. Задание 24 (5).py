def max_dist(s):
    m = []
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            count += 1
            if s[i] == s[j]:
                m.append(count)
                count = 0
    return max(m)


a = [i for i in open('files\\102.txt').read().splitlines() if i.count("G") < 15]
mx = []
for i in a:
    mx.append(max_dist(i))
print(max(mx))