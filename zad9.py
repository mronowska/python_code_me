#zgadywanie wylosowanej liczby

import random
wylosowana_liczba = random.randint(1, 101)
print(f"Nie mów nikomu, ale wylosowana liczba to: {wylosowana_liczba}")

liczba = int(input("Podaj liczbę: "))

while True:
    if liczba == wylosowana_liczba:
        print("WOW!! Wygrałeś/aś!")
        break
    if liczba < wylosowana_liczba:
        print("Podana liczba jest za mała, spróbuj ponownie...")
    if liczba > wylosowana_liczba:
        print("Podana liczba jest za duża, spróbuj ponownie!")
    liczba = int(input("Podaj liczbę: "))


