s = input()

temp = ""
arr = []

for i in range(len(s)):
    if s[i] != " ":
        temp += s[i]
    if s[i] == " " or i == len(s) - 1:
        arr.append(int(temp))
        temp = ""
        
index_min = arr.index(min(arr))
index_max = arr.index(max(arr))
tmp = max(arr)
arr[index_max] = min(arr)
arr[index_min] = tmp

print(arr)
