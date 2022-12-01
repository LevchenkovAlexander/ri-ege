table = ""

for i in range(1, 11):
    for j in range(1, 11):
        table += str(i) + " * " + str(j) + " = " + str(i * j) + " "
    table += "\n"
print(table)
