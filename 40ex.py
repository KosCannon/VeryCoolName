noise_levels = {
    130: "Отбойный молоток",
    106: "Газовая газонокосилка",
    70: "Будильник",
    40: "Тихая комната"
}

decibels = int(input("Введите уровень шума в децибелах: "))

if decibels in noise_levels:
    print(f"Уровень шума {decibels} дБ соответствует {noise_levels[decibels]}.")
elif decibels > max(noise_levels.keys()):
    print(f"Уровень шума {decibels} дБ выше максимального уровня шума в таблице ({max(noise_levels.keys())} дБ).")
elif decibels < min(noise_levels.keys()):
    print(f"Уровень шума {decibels} дБ ниже минимального уровня шума в таблице ({min(noise_levels.keys())} дБ).")
else:
    for level in sorted(noise_levels.keys()):
        if decibels < level:
            print(f"Уровень шума {decibels} дБ находится между {level - 10} дБ и {level} дБ.")
            break
