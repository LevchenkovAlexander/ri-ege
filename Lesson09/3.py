_city1 = input()
_city2 = input()
_city3 = input()

city1 = len(_city1)
city2 = len(_city2)
city3 = len(_city3)

short_name = ""
long_name = ""

if city1 > city2 > city3:
    long_name = _city1
    if city2 > city3:
        short_name = _city3
    else:
        short_name = _city2
elif city2 > city1 > city3:
    long_name = _city2
    if city1 > city3:
        short_name = _city3
    else:
        short_name = _city1
elif city3 > city2 > city1:
    long_name = _city3
    if city1 > city2:
        short_name = _city2
    else:
        short_name = _city1
        
print(short_name)
print(long_name)