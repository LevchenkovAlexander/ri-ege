num = input()
cnt = 0
while num != "0":
    if "9" in num:
        cnt += 1
    num = input()
print(cnt)