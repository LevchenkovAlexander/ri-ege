a = open("files\\104.txt").read()
str = 0
max_str = str
dot_count = 0
for i in a:
    if i == ".": dot_count += 1
    if dot_count < 5: str += 1
    else: 
        max_str = max(max_str, str)
        str = 0
        dot_count = 0
         
print(max_str)