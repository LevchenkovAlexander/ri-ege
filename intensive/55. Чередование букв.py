word = input()

alf = "bcdfghjklmnpqrstvwxz"
alf1 = "aeioy"

word = word.lower()

out = False
for i in range(len(word)-1):
    if word[i] in alf1 and word[i+1] in alf or word[i] in alf and word[i+1] in alf1:
        out = True
print("Yes" if out else "No")
