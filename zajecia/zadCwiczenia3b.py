# słowniki

osoba = {} # osoba = dict()
print(osoba)

osoba["imię"] = "Monika"
osoba["nazwisko"] = "Banan"
osoba["wiek"] = 124

# wydobycie wartości poprzez klucz
print(osoba["imię"])

# wyświetlanie wszystkich kluczy słownika
print(osoba.keys())

print("------------------")
## iterowanie po słownikach

# wartości (same klucze to i)
for i in osoba:
    print(osoba[i])

# klucz i wartość
for i in osoba:
    print (f"{i} => {osoba[i]}")

# przez items
for klucz, wartosc in osoba.items():
    print(f"{klucz} => {wartosc}")

