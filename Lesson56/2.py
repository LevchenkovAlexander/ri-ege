def read(file):
    data = []
    sm = 0
    for i in file.read().splitlines()[1:]:
        if int(i) < 51:
            sm += int(i)
        else:
            data.append(int(i))
    return sm, data

sm, data = read(open(f"Lesson56/{input()}.txt"))

data.sort(reverse= True)
discount = []

for i in range(int(len(data) / 2)):
    discount.append(data.pop())

print(sum(data) + int((f:=sum(discount)) - f/4) + 1 + sm, discount[-1])