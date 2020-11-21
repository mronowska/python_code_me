import random
import sys
import csv
import initial
import ask_and_answer
import colors

def fifty_fifty(questions, question_number, right_answer_number):
    print(f"\n{colors.colors.WARNING}50/50 - to Twój wybór!{colors.colors.ENDC} Oto pozycje, które zostają (pozostałe dwie odrzucamy!)\n")
    first_option = right_answer_number
    sec_option = initial.random.randint(0, 4)
    while first_option == sec_option:
        sec_option = initial.random.randint(0, 4)
    print(f"{colors.colors.OKGREEN}Pozostają opcje: {questions[int(question_number)][int(first_option) + 1]} oraz {questions[int(question_number)][int(sec_option) + 1]}{colors.colors.ENDC}! Pozostałe odrzucamy...")
    index = initial.lifebuoys.index("50/50")
    del initial.lifebuoys[index]