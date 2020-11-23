# 7 wyjątków

def keyboardInterrupt_error():
    dic = {"Pierwszy" : 23,
           "Drugi: " : 25}
    try:
        print(dic["Trzeci"])
    except KeyError:
        print("Brak klucza")

def nameError_error():
    try:
        sdfsdfdsf
    except NameError:
        print("Brak definicji")

def valueError_error():
    try:
        int("sfsdfsf")
    except ValueError:
        print("Zły typ")

keyboardInterrupt_error()
nameError_error()
valueError_error()