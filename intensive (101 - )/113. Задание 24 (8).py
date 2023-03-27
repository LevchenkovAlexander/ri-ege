a = open("files/113.txt").read()
count = 0

for i in range(len(a) - 2):
    n = a[i:i+3]
    if n == "TIK" or n == "TOK":
        count += 1
        print(n)
print(count)