def oblicz_wyplate(liczba_godzin, nadgodziny, stawka):
    wyplata = liczba_godzin * stawka + 1.5 * nadgodziny * stawka
    return wyplata

liczba_godzin = int(input("Ile godzin przepracowałeś/aś? "))
nadgodziny = int(input("A ile miałeś nadgodzin? "))
stawka = int(input("Jaka jest Twoja stawka?"))

print(oblicz_wyplate(liczba_godzin, nadgodziny, stawka))