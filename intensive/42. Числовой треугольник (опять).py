n = int(input())
triangle = ""
num = 0

for i in range(n):
    for j in range(i+1):
        num += 1
        triangle += str(num) + " "
    triangle += "\n"

print(triangle)
