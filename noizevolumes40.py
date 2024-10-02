def check_noise_level(noise_level):

  noise_levels = {
    130: "Отбойный молоток",
    106: "Газовая газонокосилка",
    70: "Будильник",
    40: "Тихая комната"
  }

  if noise_level in noise_levels:
    print(f"Уровень шума {noise_level} дБ соответствует: {noise_levels[noise_level]}")
  elif noise_level > 130:
    print("Введенный уровень шума выше, чем максимальный уровень в таблице (130 дБ).")
  elif noise_level < 40:
    print("Введенный уровень шума ниже, чем минимальный уровень в таблице (40 дБ).")
  else:
    for level in sorted(noise_levels.keys()):
      if noise_level < level:
        print(f"Введенный уровень шума {noise_level} дБ находится между {noise_levels[level - 1]} ({level - 1} дБ) и {noise_levels[level]} ({level} дБ).")
        break

while True:
  try:
    noise_level = int(input("Введите уровень шума в децибелах: "))
    check_noise_level(noise_level)
    break
  except ValueError:
    print("Некорректный ввод. Введите число.")