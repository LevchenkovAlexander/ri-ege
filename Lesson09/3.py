city1 = input()
city2 = input()
city3 = input()

if len(city1) > len(city2) > len(city3):
    print(city1)
elif len(city2) > len(city1) > len(city3):
    print(city2)
else:
    print(city2)


