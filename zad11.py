#zadanie 11

odleglosc = 100
sr_spalanie = 5.2
cena = 4

#ile litrów zostanie spalone w czasie trasy
def oblicz_ilosc_paliwa(dlugosc_trasy, srednie_spalanie):
    return dlugosc_trasy * srednie_spalanie / 100

#ile będzie kosztować to paliwo na całą trasę
def oblicz_koszt_paliwa(ile_litrow, cena_paliwa):
    return ile_litrow * cena_paliwa


def oblicz_koszt_podrozy(dlugosc_trasy, srednie_spalanie, cena_paliwa):
   il_paliwa = oblicz_ilosc_paliwa(odleglosc, srednie_spalanie)
   koszt_paliwa = oblicz_koszt_paliwa(il_paliwa, cena_paliwa)
   return koszt_paliwa

print(oblicz_koszt_podrozy(odleglosc, sr_spalanie, cena))