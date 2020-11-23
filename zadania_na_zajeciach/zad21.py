# zad 4 pliki
import os

tab = ["wilczarz irlandzki", "bokser", "berneński pies pasterski", "bernardyn", "collie", "doberman", "golden retriver",
       "dog niemiecki", "pudel", "golden doodle", "dziobak"]

os.makedirs("../zadania_na_zajeciach/testowy_katalog", exist_ok=True)
file = open("copy.txt", "w", encoding="utf-8")

for i in tab:
    file.write(str(tab.index(i) + 1) + '. ')
    file.write(i + '\n')

file.close()
