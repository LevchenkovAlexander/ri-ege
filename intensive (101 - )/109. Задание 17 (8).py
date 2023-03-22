a = list(map(int, open('files/109.txt')))

a = [i for i in a if i % 13 == 7 and i % 7 and i % 11]

print(max(a) - min(a))