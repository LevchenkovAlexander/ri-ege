s = input()
out = ""
start = False
for sym in s:
    if sym == " " and start:
        start = False
        continue
    out += sym
    if sym == "." or sym == "!" or sym == "?":
        out += "\n"
        start = True

print(out)
