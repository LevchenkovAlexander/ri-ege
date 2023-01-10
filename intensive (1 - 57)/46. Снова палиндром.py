def is_pol(s):
    ans = False
    tmp = ""
    for i in range(len(s)//2):
        tmp += s[i]
    for i in range(len(s) // 2, -1, -1):
        tmp += s[i]
    if tmp == s:
        return True
    return False


print(is_pol(input()))
