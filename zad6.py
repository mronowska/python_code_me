slownik = {'imie': 'Monika', 'nazwisko': 'Ronowska', 'rok_ur' : 1994, 'adres': 'Toronto 2137'}
print("{imie} {nazwisko} urodziła się w {rok_ur} i mieszka pod adresem {adres}".format(**slownik))

# imie_zmiana = input("Podaj inne imię: ")

slownik['pseudonim'] = input("Podaj pseudonim: ")
print(slownik['pseudonim'])
print(slownik)

