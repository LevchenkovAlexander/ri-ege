str = input()

if len(str) < 10:
    str = str[:6]
else:
    while len(str) < 12:
        str += "o"
print(str)