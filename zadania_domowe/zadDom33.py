def zly_numer():
    kod = input("Podaj kod pocztowy (xx-xxx): ")
    tab = []
    for i in kod:
        tab.append(i)

    try:
        print(f"Twój kod to: {int(tab[0])}{int(tab[1])}{(tab[2])}{int(tab[3])}{int(tab[4])}")
    except:
        print("Niepoprawny format kodu...")

zly_numer()