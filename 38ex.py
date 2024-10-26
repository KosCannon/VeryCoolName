sides = int(input("Введите количество сторон фигуры: "))

if sides == 3:
    print("Это треугольник.")
elif sides == 4:
    print("Это четырехугольник.")
elif sides == 5:
    print("Это пятиугольник.")
elif sides == 6:
    print("Это шестиугольник.")
elif sides == 7:
    print("Это семиугольник.")
elif sides == 8:
    print("Это восьмиугольник.")
elif sides == 9:
    print("Это девятиугольник.")
elif sides == 10:
    print("Это десятиугольник.")
else:
    print("Количество сторон должно быть от 3 до 10.")
