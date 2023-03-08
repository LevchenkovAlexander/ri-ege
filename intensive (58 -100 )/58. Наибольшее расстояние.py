str = input()
max_len = 1
str = str.lower()
for i in str:
    tmp = str[str.find(i) + 2:]
    tmp = tmp[:tmp.find(i)]
    if len(tmp) > max_len:
        max_len = len(tmp)
    
print(max_len)
