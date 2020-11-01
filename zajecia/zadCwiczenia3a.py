#krotki (tuple) - nawiasy okrągłe, nie można jej modyfikować, więcej na slajdach

dni_tyg = ("pon", "wt", "sr", "czw", "pt")

print(dni_tyg[0])
print(type(dni_tyg))

#aby ją zmodyfikować, trzeba zamienić na listę, wtedy to zrobić, potem znów na krotkę :)

#krotka -> lista
lista = list(dni_tyg)
print(type(lista))

#modyfikacja
lista[0] = "piąteczek"

#lista -> krotka
dni_tyg = tuple(lista)

print(dni_tyg)


#rozpakowywanie krotki
pon, wt, sr, czw, pt = dni_tyg
print(pon)

#jednoelementowa krotka
krotka = ("kot",)
print(type(krotka))
