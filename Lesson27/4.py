s = input()

arr = list(map(int, s.split()))
        
index_min = arr.index(min(arr))
index_max = arr.index(max(arr))
tmp = max(arr)
arr[index_max] = min(arr)
arr[index_min] = tmp

print(arr)
