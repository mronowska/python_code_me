# zadanie 3

cena = 50
wiek = int(input("Podaj swój wiek: "))


if wiek > 15:
    stan_konta = int(input("Podaj stan konta: "))
    if  cena < stan_konta:
        print("Zapraszamy na seans!")
    else:
        print("Stary jesteś, ale masz za mało $$$... Przykro mi.")
else:
    print("Niestety jesteś za młody/a...")