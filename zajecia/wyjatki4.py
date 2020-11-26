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
        print("Zła wartość")

def typeError_error():
    try:
        zmienna = "sdfsdgdfgfdg" + 7
    except TypeError:
        print("Zły typ")

def moduleNotFoundError_error():
    try:
        import Monia
    except ModuleNotFoundError:
        print("Modułu nie znaleziono")

# def syntaxError_error():
#     try:
#         print("sfsdfsdf'sdfsdsss"dd"dfsfsdf")
#     except SyntaxError:
#         print("Błąd składni")


keyboardInterrupt_error()
nameError_error()
valueError_error()
typeError_error()
moduleNotFoundError_error()
syntaxError_error()