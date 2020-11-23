#number = input("Podaj liczbę: ")

# #składnia na wyjątek
# try:
#     var1 = int(number)
#     print(var1)
# except:
#     print("Błąd")
#
# print(var1)

def get_number():
    while True:
        number = input("Podaj liczbę: ")
        try:
            return float(number)
        except:
            print("Błędna liczba")
            continue

#number = get_number()
print(get_number())