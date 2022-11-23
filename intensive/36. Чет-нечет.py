string = input()
odd = 0
even = 0

for i in range(len(string)):
    if int(string[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    output = "четных: " + str(even)
elif odd > even:
    output = "нечетных: " + str(odd)
else:
    output = "равное кол-во чет и нечет"

print(output)
