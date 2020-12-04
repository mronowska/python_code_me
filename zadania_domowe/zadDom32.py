serduszko = {
    "wafelek" : "kit kat",
    "muzyczka" : "hiszpańskie pieśni torreadorów",
    "zespół" : "Golec uOrkiestra",
    "kraj" : "Kanada",
    "zwierzątko" : "pieseczki"
}

def get_value():
    while True:
        key = input("Podaj klucz ze słownika: ")
        try:
            return serduszko[key]
        except:
            print("Brak podanego klucza. Spróbuj ponownie.")
            continue

print(get_value())

