conts = sorted([int(i) for i in open("Lesson56/3.txt").read().splitlines()[1:]], reverse= True)

stock = []
id = 0
while len(conts) and id < 1000:
    curr_vault = []
    for i in conts:
        if len(curr_vault) and curr_vault[-1] - 5 >= i:
            curr_vault.append(i)
            conts.remove(i)
        elif not len(curr_vault):
            curr_vault.append(i)
            conts.remove(i)
    stock.append(len(curr_vault))
    id += 1
print(len(stock), stock[0])