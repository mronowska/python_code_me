text = "cześć"
#text[0] = "C"
#nie można sobie podmieniać pod indeksem w łańcuchach. W tablicach jak najbardziej - są mutowalne

moja_lista = []
print(len(moja_lista))

moja_lista.append("poniedziałek")
print(moja_lista)

moja_lista.append("środa")
print(moja_lista)

moja_lista[1] = "czwartek"

print(moja_lista)

nowa_lista = ["pon", "wt", "sr", "czw", "pt", "sob", "niedz"]
print(nowa_lista[0].replace("pon", "pt"))
print(nowa_lista)


### Pętle

for i in nowa_lista:
    print(i)
