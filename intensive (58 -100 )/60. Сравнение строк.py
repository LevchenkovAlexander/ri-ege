s1 = input()
s2 = input()

if s1 == s2:
    print("Строки совпадают полностью")
elif s1 in s2:
    print(f"Строка {s1} вложена в строку {s2}")
elif s2 in s1:
    print(f"Строка {s2} вложена в строку {s1}")
else:
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
                print(f"Строки начинают различаться с символа {i+1}")
                break
            
