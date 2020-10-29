#zad 8 z wykładów

def pobierz_dane():
    wiek = input("Podaj wiek: ")
    return wiek

def sprawdz_czy_liczba(wiek):
    return wiek.lstrip("-").isnumeric() #lstrip - usun z lewej znak z nawiasu, isnumeric - czy liczba

def sprawdz_czy_liczba_ujemna(wiek):
    pass

def sprawdz_czy_liczba_parzysta():
    pass

def wiek_mniejszy_od_0(wiek):
    if wiek < 0:
        print("Wiek nie może być liczbą ujemną.")

def wiek_jest_parzysty(wiek):
    if wiek % 2 == 0:
        print("Wiek jest parzysty.")

def main():
    wiek_napis = pobierz_dane()
    if sprawdz_czy_liczba(wiek_napis):
        print("Jest to liczba")
    else:
        print("Nie jest to liczba")



