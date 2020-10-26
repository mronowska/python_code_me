#zgadywanie wylosowanej liczby


import random
wylosowana_liczba = random.randint(1, 101)
print(f"Nie mów nikomu, ale wylosowana liczba to: {wylosowana_liczba}")

ile_prob = 6
proba = 1
liczba = int(input(f"Podaj liczbę. Uważaj, masz tylko {ile_prob} prób: "))

while proba < ile_prob:
    if liczba == wylosowana_liczba:
        print("WOW!! Wygrałeś/aś!")
        break
    if liczba < wylosowana_liczba:
        print("Podana liczba jest za mała, spróbuj ponownie...")
    if liczba > wylosowana_liczba:
        print("Podana liczba jest za duża, spróbuj ponownie!")
    liczba = int(input("Podaj liczbę: "))
    proba += 1


