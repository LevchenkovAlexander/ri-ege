data = sorted([[int(i) for i in j.split()] for j in open(f"Lesson59/{input()}.txt").read().splitlines()[1:]])

start = 1633305600
end = start + 7*24*60*60

started = {i: 0 for i in range(start, end+1)}
ended = started.copy()
running = started.copy()

for i in data:
    if i[0] in started:
        started[i[0]] += 1
    if i[1] in ended:
        ended[i[1]] += 1
    if i[0] <= start and (i[1] > start or i[1] == 0):
        running[start] += 1

for i in started:
    if i > start:
        running[i] = running[i-1] + started[i] - ended[i]

running.pop(end)
print(f := max(list(running.values())), sum([1 for i in running.keys() if running[i] == f]))