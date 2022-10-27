color1 = input()
color2 = input()

if (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
    color = "фиолетовый"
elif (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
    color = "оранжевый"
elif color1 == "синий" and color2 == "желтый" or (color2 == "синий" and color1 == "желтый"):
    color = "зеленый"
elif color1 == color2:
    color = color1
else:
    print("Not a color")
    color = "error"


print(color)


