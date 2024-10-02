personage = int(input())
dogage = 10.5
justage = 0
if personage <= 0:
    print("ERROR: YOUR AGE < 0")
elif personage <= 2:
    justage = personage * dogage
    print(justage)
else:
    dogage == personage * 4 + 21 - 2
    print(dogage)