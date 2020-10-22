#zbiory

zbior1 = {1, 2, 3, 4, 5, 5, 6}
print(zbior1) # nie drukuje powtórzeń, tylko pojedynczy element

# dodawanie do zbioru
zbior1.add(10)
print(zbior1)

zbior = {"Monika", "Andrzej", "Jędrek", "David"}
zbior2 = {"Azor", "Reksio", "Tuptuś", "Lolek", "Bolek", "Misiek", "David", "Andrzej"}

print(zbior.intersection(zbior2)) # część wspólna zbiorów

print(zbior.difference(zbior2)) # roznice między zbiorami - weż wszystko ze zbioru A i usuń to co występuje w zbiorze B

print(zbior.union(zbior2)) # suma

zbior2.remove("Bolek") # jeśli nie ma pozycji w zbiorze, to wywali błąd

zbior2.discard("Kicia") # jeśli nie ma pozycji, to spoczko też

print(zbior2)

#sprawdzenie, czy coś jest w zbiorze
print("Reksioo" in zbior2)

