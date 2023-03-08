a = open("files\\91.txt").read()
max_ln = 1
max_sym = ""
ln = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        ln += 1
    else: 
        if max_ln < ln:
            max_sym = a[i-1]
            max_ln = ln
        ln = 1
        
print(max_sym, max_ln)