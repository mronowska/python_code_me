import random
import sys
import csv
import lifebuoys
import ask_and_answer
import initial
import colors
from faker import Faker

def name_and_category_of_your_random_friend(one_from_three, property):
    friends = [[Faker().unique.name(), initial.random_category(initial.available_categories(initial.questions))],
               [Faker().unique.name(), initial.random_category(initial.available_categories(initial.questions))],
               [Faker().unique.name(), initial.random_category(initial.available_categories(initial.questions))]
    ]
    while friends[1][1] == friends[0][1] or friends[1][1] == friends[2][1]:
        friends[1][1] = initial.random_category(initial.available_categories(initial.questions))
    while friends[2][1] == friends[0][1] or friends[2][1] == friends[1][1]:
        friends[2][1] = initial.random_category(initial.available_categories(initial.questions))

    return friends[one_from_three][property]

def who_is_your_friend():
    friend1_name = name_and_category_of_your_random_friend(0, 0)
    friend2_name = name_and_category_of_your_random_friend(1, 0)
    friend3_name = name_and_category_of_your_random_friend(2, 0)
    friend1_category = name_and_category_of_your_random_friend(0, 1)
    friend2_category = name_and_category_of_your_random_friend(1, 1)
    friend3_category = name_and_category_of_your_random_friend(2, 1)

    print(f"""{colors.colors.OKBLUE}
**** Przed rozpoczęciem gry musisz wybrać, kto dziś pomoże Ci w odpowiedzi na pytania! WHO'S YOUR FRIEND? ****{colors.colors.ENDC}\n
Możesz szukać pomocy u {colors.colors.OKGREEN}{friend1_name}{colors.colors.ENDC}, {colors.colors.OKGREEN}{friend2_name}{colors.colors.ENDC} lub u {colors.colors.OKGREEN}{friend3_name}{colors.colors.ENDC}.
Mam nadzieję, że pamiętasz:\n
>> iż mocna strona {colors.colors.BOLD}{colors.colors.OKGREEN}{friend1_name}{colors.colors.ENDC} to {colors.colors.OKGREEN}{friend1_category}{colors.colors.ENDC},
\n>> {colors.colors.BOLD}{colors.colors.OKGREEN}{friend2_name}{colors.colors.ENDC} to specjalista w kategorii {colors.colors.OKGREEN}{friend2_category}{colors.colors.ENDC},\n
>> a {colors.colors.BOLD}{colors.colors.OKGREEN}{friend3_name}{colors.colors.ENDC} to oczywiście człowiek od działu {colors.colors.OKGREEN}{friend3_category}{colors.colors.ENDC}!\n
{colors.colors.UNDERLINE}Zastanów się i wybierz rozsądnie! To może zaważyć o Twoich $$$$!\n{colors.colors.ENDC}""")

    chosen_friend = input(f"W czasie gry chcę zadzwonić do:\n\nA. {friend1_name}\nB. {friend2_name}\nC. {friend3_name}\n\n{colors.colors.BOLD}Twój wybór: {colors.colors.ENDC}").upper()
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
