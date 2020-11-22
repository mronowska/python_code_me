import random
import sys
import csv
import initial
import ask_and_answer
import colors

friend_name = ""
friend_category = ""

def phone_call(question_category, right_answer_number):
    list_of_options = ["A", "B", "C", "D"]

    if friend_category == question_category:
        friend_answer_index = right_answer_number
        print(
            f"""\n
Świetnie się składa! Na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty w tym temacie: HALLO {colors.colors.WARNING}{friend_name.upper()}{colors.colors.ENDC}!\n
DDRYYNNN.... DRYNNN... \n\nHALO?! Tu {friend_name}, tak, tak, widzę pytanie... Krótka piłka, bo pytanie jest proste jak kijek, ale wiesz, taki naprawę prosty. {colors.colors.OKCYAN}Prawidłowa odpowiedź to {list_of_options[int(friend_answer_index)]}. Wybierz {list_of_options[int(friend_answer_index)]}!{colors.colors.ENDC}\n
            """)

    else:
        friend_answer_index = random.randint(0, 3)
        print(
            f"""\n
Ciekawe... Czy to nie jest zbyt ryzykowne, aby na pytanie dotyczące tematu {question_category} dzwonimy do specjalisty temacie {friend_category}? 
Niestety, nie ma już powrotu, trzymamy kciuki! HALO {colors.colors.WARNING}{friend_name.upper()}{colors.colors.ENDC}!\n
DRYYNNN.... DRYNNN... HALO?! Tu {friend_name}, tak, tak, widzę pytanie... Słuchaj, nie mam pewności na sto procent, ale gdyby naprawdę... O jenki... Za takie pieniądze... Ziomek... No nic... Słuchaj - ja stawiam na odpowiedź B! Nie... A?... OSTATECZNIE {list_of_options[int(friend_answer_index)]}! Wybierz {list_of_options[int(friend_answer_index)]}!{colors.colors.ENDC}\n""")

    #usunięcie telefonu do przyjaciela z listy kół ratunkowych
    index = initial.lifebuoys.index("telefon do przyjaciela")
    del initial.lifebuoys[index]