n = int(input())
n = str(n)
is_pol = True
k = len(n) - 1
for i in range(len(n)):
    if n[i] != n[k-i]:
        is_pol = False
        break

print(is_pol)
