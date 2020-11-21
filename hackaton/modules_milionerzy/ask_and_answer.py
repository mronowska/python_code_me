import random
import csv
import sys
import initial
import lifebuoys
import colors

def analyze_answer(questions, question_number):

    choices = {
                  "A" : 0,
                  "B" : 1,
                  "C" : 2,
                  "D" : 3
    }
    # del questions[question_number]
    print(f"{colors.colors.HEADER}\nPozwól, że powtórzę pytanie nr {question_number + 1}: {questions[question_number][0]}{colors.colors.ENDC}\n")
    print("Wskaż poprawną odpowiedź!")
    print(f"{colors.colors.OKCYAN}Odpowiedź A: {questions[question_number][1]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź B: {questions[question_number][2]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź C: {questions[question_number][3]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź D: {questions[question_number][4]}\n{colors.colors.ENDC}")
    choice = input("Twoja odpowiedź na pytanie: ").upper()
    while choice not in choices:
        print("{colors.colors.BOLD}Niepoprawny znak... Wpisz odpowiedź w formie litery: A, B, C lub D!")
        choice = input("Twoja odpowiedź: ").upper()
    print(f"{colors.colors.BOLD}Wybrana przez Ciebie odpowiedź, to {choice}{colors.colors.ENDC}")
    if int(choices[choice]) == int(questions[question_number][5]):
         print(f"""{colors.colors.BOLD}{colors.colors.WARNING}PRAWIDLOWA ODPOWIEDŹ! Niesamowite!\n
         Masz na koncie aż {initial.add_score(question_number)} zł!!! $$${colors.colors.ENDC}""")
         if question_number == 11:
             print(f"""{colors.colors.BOLD}{colors.colors.WARNING}$$$$$$$$$$$$$$$$$$$$$$$$$ JESTEŚ ZWYCIĘZCĄ $$$$$$$$$$$$$$$$$$$$$$$$$\n----------------------- KONIEC GRY -----------------------{colors.colors.ENDC}""")

    else:
        # klucz litery
        print(f"""\n{colors.colors.BOLD}{colors.colors.FAIL}Przykro mi, ale jesteś WIELKIM PRZEGRANYM! Poprawna odpowiedź na to pytanie to {choice}\n----------------------- KONIEC GRY -----------------------""")
        sys.exit(0)

def ask_question(questions, question_number):
    lifebuoys_flag = False
    print(f"""{colors.colors.HEADER}\n###################################################################\nPytanie numer {question_number+1}: {questions[question_number][0]}\n###################################################################\n{colors.colors.ENDC}""")
    #del questions[question_number]
    print("Wskaż poprawną odpowiedź!")
    print(f"{colors.colors.OKCYAN}Odpowiedź A: {questions[question_number][1]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź B: {questions[question_number][2]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź C: {questions[question_number][3]}{colors.colors.ENDC}")
    print(f"{colors.colors.OKCYAN}Odpowiedź D: {questions[question_number][4]}\n{colors.colors.ENDC}")


    if len(initial.lifebuoys) > 0 and lifebuoys_flag is False:
        print(f"""{colors.colors.HEADER}Pamiętaj, że możesz skorzystać z kół ratunkowych! Na tę chwilę masz do wyboru jeszcze:{colors.colors.ENDC}""")
        for lifebuoy in initial.lifebuoys:
            print(f"{colors.colors.HEADER}>>>>>>>>> {colors.colors.BOLD}{lifebuoy}{colors.colors.ENDC}")
        is_lifebuoy = input("\nCzy chcesz skorzystać z koła ratunkowego?[t/n]: ").upper()
        while (is_lifebuoy != "T" and is_lifebuoy != "N"):
            print(
                "Wprowadzony znak jest niepoprawny. Wpisz 't' jeśli chcesz skorzystać z pomocy lub 'n' jeśli nie chcesz")
            is_lifebuoy = input("Czy chcesz skorzystać z koła ratunkowego?[t/n]: ").upper()
        if is_lifebuoy == "T":
            lifebuoys.func_lifebuoys(questions, question_number)
            lifebuoys_flag = True
            wait = input()
        if is_lifebuoy == "N":
            analyze_answer(questions, question_number)
    else:
        print(f"{colors.colors.FAIL}\n********************************************************************{colors.colors.ENDC}")
        print(f"{colors.colors.FAIL}Wykorzystałeś już wszystkie koła ratunkowe! Musisz radzić sobie sam...{colors.colors.ENDC}")
        print(f"{colors.colors.FAIL}********************************************************************\n{colors.colors.ENDC}")

        analyze_answer(questions, question_number)