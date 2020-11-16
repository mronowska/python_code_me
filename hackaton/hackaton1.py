#### milionerzy

### questions - na przyszłość pobierać z pliku ###

import random
import sys


questions = [
    ["Pyt. 1: Polskim odpowiednikiem baby shower jest:", "bociankowe", "prysznicowe", "500+", "becikowe", 0],
    ["Pyt. 2: W piosence Dwa plus Jeden pada propozycja: 'Chodź pomaluj mój świat...", "niech wygląda jak kwiat'", "mam już dość szarych krat'", "na żółto i na niebiesko'", "bo świat jest dziś pod kreską'", 2],
    ["Pyt. 3: Co jest tradycyjnym środkiem transportu amiszów?", "motorówka", "zaprzęg", "śnieżny skuter", "motocykl", 1],
    ["Pyt. 4: Pęd wyrosły z nieuszlachetnionej podkładki to:", "kot albo pies", "wilk albo dzik", "koń albo krowa", "baran albo kozioł", 1],
    ["Pyt. 5: Tytułowa wataha z serialu wyreżyserowanego m.in. przez Kasię Adamik to:", "wilcza rodzina", "rosyjscy szpiedzy", "strażnicy graniczni", "uchodźcy ze Wschodu", 2],
    ["Pyt. 6: Których bierek w bierkach jest najwięcej?", "wioseł", "bosaków", "trójzębów", "oszczepów", 3],
    ["Pyt. 7: W jakiej bitwie miał swój udział sławny w Polsce i Szkocji kapral niedźwiedź o imieniu Wojtek?", "pod Grunwaldem", "pod Wiedniem", "pod Monte Cassino", "o Anglię", 2],
    ["Pyt. 8: Aorta wychodzi z lewej komory serca, a kończy się:", "w prawej komorze", "w jamie brzusznej", "w płucach", "w mózgu", 1],
    ["Pyt. 9: Autor dwóch pozycji - 'Książki, którą napisałem, żeby mieć na dziwki i narkotyki' i 'Książki, którą napisałem, żeby mieć na odwyk' to:", "Marek Raczkowski", "Maciej Maleńczuk", "Kamil Durczok", "Witkacy", 3],
    ["Pyt. 10: Symbol waluty euro to stylizowana litera grecka. Która?", "beta", "heta", "eta", "epsilon", 3],
["Pyt. 11: Za 30 judaszowych srebrników arcykapłani kupili kawałek ziemi nazywany Polem Garncarza, który przeznaczyli na:", "plantację oliwek", "wybieg dla lwów", "cmentarz dla cudzoziemców", "targowisko", 2],
["Pyt. 12 ZA MILION!!!!: Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121", "12 321", "1 234 321", "111 111 111", "123 454 321", 1]
]

lifebuoys = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]

def add_score(question_number):
    score = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
    return score[question_number]

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

def fifty_fifty(questions, question_number, right_answer_number):
    print("50/50 - to Twój wybór! Oto pozycje, które zostają (pozostałe dwie odrzucamy!)")
    first_option = right_answer_number
    sec_option = random.randint(0, 4)
    print(sec_option)
    while first_option == sec_option:
        sec_option = random.randint(0, 4)
    print(f"Pozostają opcje: {questions[question_number][first_option+1]} oraz {questions[question_number][sec_option+1]}! Pozostałe odrzucamy...")
    index = lifebuoys.index("50/50")
    del lifebuoys[index]

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
         print(f"Masz na koncie aż {add_score(question_number)} zł!!! $$$")
         if question_number == 11:
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
        fifty_fifty(questions, question_number, questions[question_number][5])
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
            func_lifebuoys(questions, question_number)
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