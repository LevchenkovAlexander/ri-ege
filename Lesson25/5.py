for i in range(101, 200):
    s = "1" * i 
    while '111' in s:
        s = s.replace("111", "22", 1).replace("222", "11", 1)
    if s.count("1") == 1: # сначала проверяем 0, если при 0 ничего не вывело, значит проверяем 1 и тд
        print(i)
        break
   
    