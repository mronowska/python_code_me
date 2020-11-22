import random
import sys
import csv
import initial
import ask_and_answer
import colors

def audience():
    print("\nProszę Państwa... Proszę o głosy! <klik><klik><szumy><szumy> Ach tak, już widzę... Oczywiście. Oto wyniki publiczności:")
    answer_a = initial.random.randint(0, 100)
    answer_b = initial.random.randint(0, 100 - answer_a)
    answer_c = initial.random.randint(0, 100 - answer_a - answer_b)
    answer_d = 100 - answer_a - answer_b - answer_c
    print(f"""{colors.colors.WARNING}
Na odpowiedź A zagłosowało: {answer_a}% osób
Odpowiedź B: {answer_b}% osób
Z kolei na odpowiedź C: {answer_c}% osób
I wreszczie na odpowiedź D: {answer_d}% osób
{colors.colors.ENDC}
Czy w czymś Ci to pomogło? Nakierowało? Teraz musisz wybrać!\n
    """)

    #usunięcie opcji pytania do publiczności z kół ratunkowych
    index = initial.lifebuoys.index("pytanie do publiczności")
    del initial.lifebuoys[index]