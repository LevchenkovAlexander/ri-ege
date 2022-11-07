str1 = input()
str2 = input()
str3 = input()

if len(str1) < len(str2) and len(str1) < len(str3):
    if len(str2) < len(str3):
        if (len(str2) - len(str1)) == (len(str3) - len(str2)):
            print("YES")
        else:
            print("NO")
    else:
        if (len(str3) - len(str1)) == (len(str2) - len(str3)):
            print("YES")
        else:
            print("NO")
elif len(str2) < len(str1) and len(str2) < len(str3):
    if len(str1) < len(str3):
        if (len(str1) - len(str2)) == (len(str3) - len(str1)):
            print("YES")
        else:
            print("NO")
    else:
        if (len(str3) - len(str2)) == (len(str1) - len(str3)):
            print("YES")
        else:
            print("NO")
elif len(str3) < len(str2) and len(str3) < len(str1):
    if len(str1) < len(str2):
        if (len(str1) - len(str3)) == (len(str2) - len(str1)):
            print("YES")
        else:
            print("NO")
    else:
        if (len(str2) - len(str3)) == (len(str1) - len(str2)):
            print("YES")
        else:
            print("NO")
elif len(str1) == len(str2) == len(str3):
    print("NO")




