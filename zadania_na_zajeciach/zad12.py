liczba_godzin = int(input("Ile godzin przepracowałeś/aś? "))
stawka = int(input("Jaka jest Twoja stawka?"))

def oblicz_wyplate(liczba_godzin, stawka):
    wyplata1 = liczba_godzin * stawka
    wyplata2 = 0
    if liczba_godzin > 160:
        wyplata2 = (liczba_godzin - 160) * 1.5 * stawka
    return wyplata1 + wyplata2

print(oblicz_wyplate(liczba_godzin, stawka))