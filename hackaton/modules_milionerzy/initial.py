import random
import sys
import csv
import lifebuoys
import colors
import ask_and_answer
from faker import Faker

# globalna lista kół ratunkowych
lifebuoys = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]

# globalnie otwieramy plik z pytaniami, odpowiedziami, ich kategoriami
with open('pytania.csv', 'r', encoding='utf-8') as questions:
    questions = list(csv.reader(questions, delimiter=','))


def available_categories(questions_file):
    categories = []  # deklaracja pustej listy
    for category in questions:
        categories.append(category[6])
    return categories


# losuj randomową kategorię pytań
def random_category(categories):
    index_of_category = random.randint(0, len(categories) - 1)
    return categories[index_of_category]


def add_score(question_number):
    score = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
    return score[question_number]


def welcome():
    print(
        f"""
        {colors.colors.HEADER}
---------------------------Witaj w grze Milionerzy!---------------------------
-------------Odpowiedz poprawnie na 10 pytań i wygraj milion $$$$-------------{colors.colors.ENDC}
{colors.colors.BOLD}\n
Aby przejść do kolejnej treści/części gry, kliknij dowolny klawisz :){colors.colors.ENDC}\n
{colors.colors.OKBLUE}
O GRZE:\n
****** Dostępne koła ratunkowe: {lifebuoys[0]}, {lifebuoys[1]}, {lifebuoys[2]}! ******{colors.colors.ENDC}
        """)
