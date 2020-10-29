def oblicz_wyplate(liczba_godzin, nadgodziny, stawka):
    wyplata1 = liczba_godzin * stawka
    if liczba_godzin > 160:
        wyplata2 =(liczba_godzin - 160)*1.5*stawka
    return wyplata1 + wyplata2

liczba_godzin = int(input("Ile godzin przepracowałeś/aś? "))
nadgodziny = int(input("A ile miałeś nadgodzin? "))
stawka = int(input("Jaka jest Twoja stawka?"))

print(oblicz_wyplate(liczba_godzin, nadgodziny, stawka))