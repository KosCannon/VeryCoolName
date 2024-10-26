while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    if number % 2 == 0:
        print(number, "- Чётное")
    else:
        print(number, "- Нечётное")