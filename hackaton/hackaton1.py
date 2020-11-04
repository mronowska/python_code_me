#### milionerzy

### questions - na przyszłość pobierać z pliku ###

import random
import sys

questions = [
    ["Pyt. 1: Polskim odpowiednikiem baby shower jest:", "bociankowe", "prysznicowe", "500+", "becikowe", 0],
    ["Pyt. 2: ", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["Pyt. 3: Czego zakręcane wieczko ma taneczną nazwę?", "szkatułki", "puderniczki", "trumienki", "słoiczka", 3],
    ["4W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["5W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["6W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["7W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["8W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["9W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3],
    ["0W którym z miast znajdują się korty Flushing Meadows?", "W Londynie", "W Paryżu", "W Nowym Jorku", "We Wiedniu", 3]
]

lifebuoys = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]

def welcome():
    print("--------Witaj w grze Milionerzy!--------\n")
    print("---Odpowiedz poprawnie na 10 pytań i wygraj milion $$$$---\n")
    print("Dostępne koła ratunkowe: pytanie do publiczności, telefon do przyjaciela, 50/50!")

def phone_call():
    print("\nDRYYNNN.... DRYNNN... HALO?! Tu Andrzej, tak, tak, widzę pytanie... Słuchaj, nie jestem pewien na sto procent, ale gdybym naprawdę... O jenki... Za takie pieniądze... Ziomek, miałbym tyle czipsów.. No nic... Słuchaj - ja bym wybrał odpowiedź B! Nie... A?... OSTATECZNIE C! Wybierz C!\n")
    index = lifebuoys.index("telefon do przyjaciela")
    del lifebuoys[index]

def audience():
    print("\nProszę Państwa... Proszę o głosy! <klik><klik><szumy><szumy> Ach tak, już widzę... Oczywiście. Oto wyniki publiczności:")
    answer_a = random.randint(0, 100)
    answer_b = random.randint(0, 100 - answer_a)
    answer_c = random.randint(0, 100 - answer_a - answer_b)
    answer_d = 100 - answer_a - answer_b - answer_c
    print(f"Na odpowiedź A zagłosowało: {answer_a}% osób")
    print(f"Odpowiedź B: {answer_b}% osób")
    print(f"Z kolei na odpowiedź C: {answer_c}% osób")
    print(f"I wreszczie na odpowiedź D: {answer_d}% osób")
    print("Czy w czymś Ci to pomogło? Nakierowało? Teraz musisz wybrać!\n")
    index = lifebuoys.index("pytanie do publiczności")
    del lifebuoys[index]

def fifty_fifty():
    print("50/50 - to Twój wybór! Oto pozycje, które zostają (pozostałe dwie odrzucamy!)")
    first_option = random.randint(0, 4)
    sec_option = random.randint(0, 4)
    while first_option == sec_option:
        sec_option = random.randint(0, 4)
    index = lifebuoys.index("50/50")
    del lifebuoys[index]

    ##tu do poprawy - trzeba znać poprawną odpowiedź i na tym się oprzeć

def analyze_answer(questions, question_number):
    choices = {
                  "A" : 0,
                  "B" : 1,
                  "C" : 2,
                  "D" : 3
    }
    choice = input("Twoja odpowiedź na pytanie: ").upper()
    while choice not in choices:
        print("Niepoprawny znak... Wpisz odpowiedź w formie litery: A, B, C lub D!")
        choice = input("Twoja odpowiedź: ").upper()
    print(f"Wybrana przez Ciebie odpowiedź, to {choice}")
    if choices[choice] == questions[question_number][5]:
         print("PRAWIDLOWA ODPOWIEDŹ! Niesamowite!")
         print(question_number)
         if question_number == 9:
             print("$$$$$$$$$$$$$$$$$$$$$$$$$ JESTEŚ ZWYCIĘZCĄ $$$$$$$$$$$$$$$$$$$$$$$$$")
             print("----------------------- KONIEC GRY -----------------------")

    else:
        # klucz litery
        print(f"\nPrzykro mi, ale jesteś WIELKIM PRZEGRANYM! Poprawna odpowiedź na to pytanie to {choice}\n")
        print("----------------------- KONIEC GRY -----------------------")
        sys.exit(0)

def func_lifebuoys(questions, question_number):
    print(f"\nWybrałeś koło ratunkowe! Z którego chcesz skorzystać?")
    if lifebuoys.count("telefon do przyjaciela") != 0:
        print("A. Telefon do przyjaciela")
    if lifebuoys.count("pytanie do publiczności") != 0:
        print("B. Pytanie do publiczności")
    if lifebuoys.count("50/50") != 0:
        print("C. 50/50")
    chosen_lifebuoy = input("Wybieram koło: ").upper()
    while chosen_lifebuoy != "A" and chosen_lifebuoy != "B" and chosen_lifebuoy != "C":
        print("Niepoprawna wartość... spróbuj jeszcze raz.")
        chosen_lifebuoy = input("Twój wybór: ").upper()
    if chosen_lifebuoy == "A":
        phone_call()
        analyze_answer(questions, question_number)
    if chosen_lifebuoy == "B":
        audience()
        analyze_answer(questions, question_number)
    if chosen_lifebuoy == "C":
        fifty_fifty()
        analyze_answer(questions, question_number)


def ask_question(questions, question_number):
    lifebuoys_flag = False
    print("\n###################################################################")
    print(f"Pytanie numer {question_number+1}: {questions[question_number][0]}")
    print("###################################################################\n")
    #del questions[question_number]
    print("Wskaż poprawną odpowiedź!")
    print(f"Odpowiedź A: {questions[question_number][1]}")
    print(f"Odpowiedź B: {questions[question_number][2]}")
    print(f"Odpowiedź C: {questions[question_number][3]}")
    print(f"Odpowiedź D: {questions[question_number][4]}\n")
    if len(lifebuoys) > 0 and lifebuoys_flag is False:
        print("********************************************************************")
        print("Pamiętaj, że możesz skorzystać z kół ratunkowych! Na tę chwilę masz do wyboru jeszcze:")
        for lifebuoy in lifebuoys:
            print(f">>>>>>>>> {lifebuoy}")
        print("********************************************************************")
        is_lifebuoy = input("\nCzy chcesz skorzystać z koła ratunkowego?[t/n]: ").upper()
        while (is_lifebuoy != "T" and is_lifebuoy != "N"):
            print(
                "Wprowadzony znak jest niepoprawny. Wpisz 't' jeśli chcesz skorzystać z pomocy lub 'n' jeśli nie chcesz")
            is_lifebuoy = input("Czy chcesz skorzystać z koła ratunkowego?[t/n]: ").upper()
        if is_lifebuoy == "T":
            func_lifebuoys()
            lifebuoys_flag = True
            wait = input()
        if is_lifebuoy == "N":
            analyze_answer(questions, question_number)
    else:
        print("\n********************************************************************")
        print("Wykorzystałeś już wszystkie koła ratunkowe! Musisz radzić sobie sam...")
        print("********************************************************************\n")


def play():
    welcome()
    question_num = 0
    while question_num < 10:
        ask_question(questions, question_num)
        question_num = question_num + 1

play()
