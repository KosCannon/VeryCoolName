notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

note_input = input("Введите ноту: ")

try:
    note = note_input[0].upper()
    octave = int(note_input[1])

    if note in notes:
        frequency = notes[note]
        frequency *= (1/2) * (4 - octave) 
        print(f"Частота {note_input} - {frequency:.2f} Гц")
    else:
        print("Ошибка")

except (IndexError, ValueError):
    print("Ошибка")
