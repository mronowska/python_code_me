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
        print(f"\nŚwietnie się składa! Na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty w tym temacie: HALLO {bcolors.WARNING}{friend_name.upper()}{bcolors.ENDC}!\n")
        print(f"""DRYYNNN.... DRYNNN... \n\nHALO?! Tu {friend_name}, tak, tak, widzę pytanie... Krótka piłka, bo pytanie jest proste jak kijek, ale wiesz, taki naprawę prosty. {bcolors.OKCYAN}Prawidłowa odpowiedź to {list_of_options[int(friend_answer_index)]}. Wybierz {list_of_options[int(friend_answer_index)]}!{bcolors.ENDC}\n""")
    else:
        friend_answer_index = random.randint(0, 3)
        print(f"\nCiekawe... Czy to nie jest zbyt ryzykowne, aby na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty temacie {friend_category}? Niestety, nie ma już powrotu, trzymamy kciuki! HALO {bcolors.WARNING}{friend_name.upper()}{bcolors.ENDC}!")
        print(f"\nDRYYNNN.... DRYNNN... HALO?! Tu {friend_name}, tak, tak, widzę pytanie... Słuchaj, nie mam pewności na sto procent, ale gdyby naprawdę... O jenki... Za takie pieniądze... Ziomek... No nic... Słuchaj - ja stawiam na odpowiedź B! Nie... A?... OSTATECZNIE {list_of_options[int(friend_answer_index)]}! Wybierz {list_of_options[int(friend_answer_index)]}!{bcolors.ENDC}\n")

    index = initial.lifebuoys.index("telefon do przyjaciela")
    del initial.lifebuoys[index]