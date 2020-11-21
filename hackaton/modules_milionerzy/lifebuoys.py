import random
import sys
import csv
import initial
import ask_and_answer
import audience
import phone_call
import fifty_fifty
import colors

def func_lifebuoys(questions, question_number):
    print(f"\nWybrałeś koło ratunkowe! Z którego chcesz skorzystać? Możesz wpisać tylko dostępne ponożej litery. Wybranie niedostępnej opcji będzie skutkować brakiem koła ratunkowego.")
    if initial.lifebuoys.count("telefon do przyjaciela") != 0:
        print(f"{colors.colors.OKBLUE}A. Telefon do przyjaciela{colors.colors.ENDC}")
    if initial.lifebuoys.count("pytanie do publiczności") != 0:
        print(f"{colors.colors.OKBLUE}B. Pytanie do publiczności{colors.colors.ENDC}")
    if initial.lifebuoys.count("50/50") != 0:
        print(f"{colors.colors.OKBLUE}C. 50/50{colors.colors.ENDC}")
    chosen_lifebuoy = input("Wybieram koło: ").upper()
    while chosen_lifebuoy != "A" and chosen_lifebuoy != "B" and chosen_lifebuoy != "C":
        print("Niepoprawna wartość... spróbuj jeszcze raz.")
        chosen_lifebuoy = input("Twój wybór: ").upper()
    if chosen_lifebuoy == "A":
        while initial.lifebuoys[0] == "telefon do przyjaciela":
            phone_call.phone_call(questions[question_number][6], questions[question_number][5])
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "B":
        audience.audience()
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "C":
        fifty_fifty.fifty_fifty(questions, question_number, questions[question_number][5])
        ask_and_answer.analyze_answer(questions, question_number)