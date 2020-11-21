import random
import sys
import csv
import lifebuoys
import ask_and_answer
from faker import Faker

lifebuoys = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]

with open('pytania.csv', 'r', encoding='utf-8') as questions:
    questions = list(csv.reader(questions, delimiter=','))

def available_categories(questions_file):
    categories = []  # deklaracja pustej listy
    for category in questions:
        categories.append(category[6])
    return categories

def random_category(categories):
    index_of_category = random.randint(0, len(categories) - 1)
    return categories[index_of_category]

def name_and_category_of_your_random_friend(one_from_three, property):
    friends = [[Faker().unique.name(), random_category(available_categories(questions))],
               [Faker().unique.name(), random_category(available_categories(questions))],
               [Faker().unique.name(), random_category(available_categories(questions))]
    ]
    while friends[1][1] == friends[0][1] or friends[1][1] == friends[2][1]:
        friends[1][1] = random_category(available_categories(questions))
    while friends[2][1] == friends[0][1] or friends[2][1] == friends[1][1]:
        friends[2][1] = random_category(available_categories(questions))

    return friends[one_from_three][property]

def who_is_your_friend():
    friend1_name = name_and_category_of_your_random_friend(0, 0)
    friend2_name = name_and_category_of_your_random_friend(1, 0)
    friend3_name = name_and_category_of_your_random_friend(2, 0)
    friend1_category = name_and_category_of_your_random_friend(0, 1)
    friend2_category = name_and_category_of_your_random_friend(1, 1)
    friend3_category = name_and_category_of_your_random_friend(2, 1)

    print(f"""
**** Przed rozpoczęciem gry musisz wybrać, kto dziś pomoże Ci w odpowiedzi na pytania! WHO'S YOUR FRIEND? ****\n
Możesz szukać pomocy u {friend1_name}, {friend2_name} lub u {friend3_name}.
Mam nadzieję, że pamiętasz, iż mocna strona {friend1_name} to {friend1_category},
{friend2_name} to specjalista w kategorii {friend2_category},
a {friend3_name} to oczywiście człowiek od działu {friend3_category}!
Zastanów się i wybierz rozsądnie! To może zaważyć o Twoich $$$$!""")

    chosen_friend = input(f"W czasie gry chcę zadzwonić do:\nA. {friend1_name}\nB. {friend2_name}\nC. {friend3_name}\nTwój wybór: ").upper()
    while chosen_friend != "A" and chosen_friend != "B" and chosen_friend != "C":
        print("Niepoprawna wartość... spróbuj jeszcze raz.")
        chosen_friend = input("Twój wybór: ").upper()
    if chosen_friend == "A":
        your_friend_tab = [friend1_name, friend1_category]
    if chosen_friend == "B":
        your_friend_tab = [friend2_name, friend2_category]
    if chosen_friend == "C":
        your_friend_tab = [friend3_name, friend3_category]

    return your_friend_tab

def add_score(question_number):
    score = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
    return score[question_number]

def welcome():
    print(f"""
---------------------------Witaj w grze Milionerzy!---------------------------
------------Odpowiedz poprawnie na 10 pytań i wygraj milion $$$$------------

Aby przejść do kolejnej treści/części gry, kliknij dowolny klawisz :)

O GRZE:

****** Dostępne koła ratunkowe: {lifebuoys[0]}, {lifebuoys[1]}, {lifebuoys[2]}! ******""")