#### milionerzy

### pytania - na przyszłość pobierać z pliku ###

pytania = [
    ["1W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu"],
    "2W którym z miast znajdują się korty Flushing Meadows?",
    "3W którym z miast znajdują się korty Flushing Meadows?",
    "4W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?",
    "W którym z miast znajdują się korty Flushing Meadows?"
]

kola = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]
print(len(kola))

def analizuj_odpowiedz():
    odpowiedz = input("Twoja odpowiedź: ").upper()
    while odpowiedz != "A" and odpowiedz != "B" and odpowiedz != "C" and odpowiedz != "D":
        print("Niepoprawny znak... Wpisz odpowiedź w formie litery: A, B, C lub D!")
        odpowiedz = input("Twoja odpowiedź: ").upper()
    print(f"Wybrana przez Ciebie odpowiedź, to {odpowiedz}")

def kola_ratunkowe():
    pass

def zadaj_pytanie(pytania, numer_pytania):
    print(f"Pytanie numer {numer_pytania}: {pytania[numer_pytania - 1][0]}\n")
    print("Wskaż poprawną odpowiedź!")
    print(f"Odpowiedź A: {pytania[numer_pytania - 1][1]}")
    print(f"Odpowiedź B: {pytania[numer_pytania - 1][2]}")
    print(f"Odpowiedź C: {pytania[numer_pytania - 1][3]}")
    print(f"Odpowiedź D: {pytania[numer_pytania - 1][4]}\n")
    if len(kola) > 0:
        print("Pamiętaj, że możesz skorzystać z kół ratunkowych! Na tę chwilę masz do wyboru jeszcze:")
        for kolo in kola:
            print(kolo)
        czy_kolo_ratunkowe = input("Czy chcesz skorzystać z koła ratunkowego?[t/n]: ").upper()
        while(czy_kolo_ratunkowe != "T" and czy_kolo_ratunkowe != "N"):
            if czy_kolo_ratunkowe == "T":
                kola_ratunkowe()
            elif czy_kolo_ratunkowe == "N":
                analizuj_odpowiedz()
            else:
                print("Wprowadzony znak jest niepoprawny. Wpisz 't' jeśli chcesz skorzystać z pomocy lub 'n' jeśli nie chcesz")
                czy_kolo_ratunkowe = input("Czy chcesz skorzystać z koła ratunkowego?[t/n]: ")
    else:
        print("Wykorzystałeś już wszystkie koła ratunkowe! Musisz radzić sobie sam...")




def graj():
    print("--------Witaj w grze Milionerzy!--------\n")
    print("---Odpowiedz poprawnie na 10 pytań i wygraj milion $$$$---\n")
    print("Dostępne koła ratunkowe: pytanie do publiczności, telefon do przyjaciela, 50/50!")
    zadaj_pytanie(pytania, 1)

graj()
