import os

print(os.listdir()) #lista plików z pliku, w którym on jest

# rozmiar plików

print(os.path.getsize("zad21OS.py"))

# stworzenie katalogu

os.makedirs("../zadania_na_zajeciach/testowy_katalog")

#z tym parametrem zabezpieczamy sie przed błędami przy wielokrotnym wykonaniu kodu. Teoretycznie możemy dodać tylko 1 katalog o tej samej nazwie, ale mając ten parametr, konsola nie walnie błędem. Jeśli już taki bedzie, to oleje, jak nie to doda.

# os.makedirs("testowy_katalog",exist_ok=True)

# usunięcie
# os.remove("testowy_katalog")

# zmiana nazwy
# os.rename("stara_nazwa", "nowa_nazwa")