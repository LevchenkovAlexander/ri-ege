inp_heights = input()
pete_height = int(input())

heights = []
tmp = ""

for i in range(len(inp_heights)):
    if inp_heights[i] != " ":
        tmp += inp_heights[i]
        
    if inp_heights[i] == " " or i == len(inp_heights)-1:
        heights.append(int(tmp))
        tmp = ""

heights.append(pete_height)
heights.sort(reverse=1)

if heights.count(pete_height) > 1:
    i = heights.index(pete_height)
    while heights[i] == pete_height:
        ind = i
        i += 1
    
else:
    ind = heights.index(pete_height)
print(ind)