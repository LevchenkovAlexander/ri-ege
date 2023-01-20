year = int(input())

diff = 0

while diff < 365:
    if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0):
        diff += 1
    year += 1
print(year, diff)
