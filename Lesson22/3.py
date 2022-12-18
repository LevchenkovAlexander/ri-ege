s = input()
a = input()

count = s.count(a)
index = "Вхождения нет" if s.find(a) == -1 else f"Первое - {s.find(a)}; последнее - {s.rfind(a)}"
s_replaced = s.replace(a, "ЗАМЕНА")

print(count, index, s_replaced, sep="\n")
