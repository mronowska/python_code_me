import random
import sys
import csv
import initial
import ask_and_answer

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

friend_name = ""
friend_category = ""

def phone_call(question_category, right_answer_number):
    list_of_options = ["A", "B", "C", "D"]

    if friend_category == question_category:
        friend_answer_index = right_answer_number
        print(f"Świetnie się składa! Na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty w tym temacie: HALLO {bcolors.WARNING}{friend_name.upper()}{bcolors.ENDC}!\n")
        print(f"""DRYYNNN.... DRYNNN... \n\nHALO?! Tu {friend_name}, tak, tak, widzę pytanie... Krótka piłka, bo pytanie jest proste jak kijek, ale wiesz, taki naprawę prosty. {bcolors.OKCYAN}Prawidłowa odpowiedź to {list_of_options[int(friend_answer_index)]}. Wybierz {list_of_options[int(friend_answer_index)]}!{bcolors.ENDC}\n""")
    else:
        friend_answer_index = random.randint(0, 3)
        print(f"Ciekawe... Czy to nie jest zbyt ryzykowne, aby na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty temacie {friend_category}? Niestety, nie ma już powrotu, trzymamy kciuki! HALO {bcolors.WARNING}{friend_name.upper()}{bcolors.ENDC}!")
        print(f"\nDRYYNNN.... DRYNNN... HALO?! Tu {friend_name}, tak, tak, widzę pytanie... Słuchaj, nie mam pewności na sto procent, ale gdyby naprawdę... O jenki... Za takie pieniądze... Ziomek... No nic... Słuchaj - ja stawiam na odpowiedź B! Nie... A?... OSTATECZNIE {list_of_options[int(friend_answer_index)]}! Wybierz {list_of_options[int(friend_answer_index)]}!{bcolors.ENDC}\n")

    index = initial.lifebuoys.index("telefon do przyjaciela")
    del initial.lifebuoys[index]

def audience():
    print("\nProszę Państwa... Proszę o głosy! <klik><klik><szumy><szumy> Ach tak, już widzę... Oczywiście. Oto wyniki publiczności:")
    answer_a = initial.random.randint(0, 100)
    answer_b = initial.random.randint(0, 100 - answer_a)
    answer_c = initial.random.randint(0, 100 - answer_a - answer_b)
    answer_d = 100 - answer_a - answer_b - answer_c
    print(f"""{bcolors.WARNING}Na odpowiedź A zagłosowało: {answer_a}% osób
Odpowiedź B: {answer_b}% osób
Z kolei na odpowiedź C: {answer_c}% osób
I wreszczie na odpowiedź D: {answer_d}% osób{bcolors.ENDC}
Czy w czymś Ci to pomogło? Nakierowało? Teraz musisz wybrać!\n""")
    index = initial.lifebuoys.index("pytanie do publiczności")
    del initial.lifebuoys[index]

def fifty_fifty(questions, question_number, right_answer_number):
    print("50/50 - to Twój wybór! Oto pozycje, które zostają (pozostałe dwie odrzucamy!)")
    first_option = right_answer_number
    sec_option = initial.random.randint(0, 4)
    while first_option == sec_option:
        sec_option = initial.random.randint(0, 4)
    print(f"Pozostają opcje: {questions[int(question_number)][int(first_option) + 1]} oraz {questions[int(question_number)][int(sec_option) + 1]}! Pozostałe odrzucamy...")
    index = initial.lifebuoys.index("50/50")
    del initial.lifebuoys[index]


def func_lifebuoys(questions, question_number):
    print(f"\nWybrałeś koło ratunkowe! Z którego chcesz skorzystać? Możesz wpisać tylko dostępne ponożej litery. Wybranie niedostępnej opcji będzie skutkować brakiem koła ratunkowego.")
    if initial.lifebuoys.count("telefon do przyjaciela") != 0:
        print("A. Telefon do przyjaciela")
    if initial.lifebuoys.count("pytanie do publiczności") != 0:
        print("B. Pytanie do publiczności")
    if initial.lifebuoys.count("50/50") != 0:
        print("C. 50/50")
    chosen_lifebuoy = input("Wybieram koło: ").upper()
    while chosen_lifebuoy != "A" and chosen_lifebuoy != "B" and chosen_lifebuoy != "C":
        print("Niepoprawna wartość... spróbuj jeszcze raz.")
        chosen_lifebuoy = input("Twój wybór: ").upper()
    if chosen_lifebuoy == "A":
        while initial.lifebuoys[0] == "telefon do przyjaciela":
            phone_call(questions[question_number][6], questions[question_number][5])
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "B":
        audience()
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "C":
        fifty_fifty(questions, question_number, questions[question_number][5])
        ask_and_answer.analyze_answer(questions, question_number)