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