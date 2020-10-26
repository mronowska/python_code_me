#napisać funkcjonalność metody index

lista = ["Mateusz", "Ania", "Andrzej", "Kamila", "Marlena"]

print(lista.index("Andrzej"))

poszukiwane_imie = "Andrzej"

for i in lista:
    pass #pusta instrukcja

pozycja = 0
for imie in lista:
    if imie == poszukiwane_imie:
        print(pozycja)
    pozycja = pozycja + 1