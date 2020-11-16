import random
import sys
import initial
import lifebuoys

def analyze_answer(questions, question_number):

    choices = {
                  "A" : 0,
                  "B" : 1,
                  "C" : 2,
                  "D" : 3
    }
    choice = input("Twoja odpowiedź na pytanie: ").upper()
    while choice not in choices:
        print("Niepoprawny znak... Wpisz odpowiedź w formie litery: A, B, C lub D!")
        choice = input("Twoja odpowiedź: ").upper()
    print(f"Wybrana przez Ciebie odpowiedź, to {choice}")
    if choices[choice] == questions[question_number][5]:
         print("PRAWIDLOWA ODPOWIEDŹ! Niesamowite!")
         print(f"Masz na koncie aż {initial.add_score(question_number)} zł!!! $$$")
         if question_number == 11:
             print("$$$$$$$$$$$$$$$$$$$$$$$$$ JESTEŚ ZWYCIĘZCĄ $$$$$$$$$$$$$$$$$$$$$$$$$")
             print("----------------------- KONIEC GRY -----------------------")

    else:
        # klucz litery
        print(f"\nPrzykro mi, ale jesteś WIELKIM PRZEGRANYM! Poprawna odpowiedź na to pytanie to {choice}\n")
        print("----------------------- KONIEC GRY -----------------------")
        sys.exit(0)

def ask_question(questions, question_number):
    lifebuoys_flag = False
    print("\n###################################################################")
    print(f"Pytanie numer {question_number+1}: {questions[question_number][0]}")
    print("###################################################################\n")
    #del questions[question_number]
    print("Wskaż poprawną odpowiedź!")
    print(f"Odpowiedź A: {questions[question_number][1]}")
    print(f"Odpowiedź B: {questions[question_number][2]}")
    print(f"Odpowiedź C: {questions[question_number][3]}")
    print(f"Odpowiedź D: {questions[question_number][4]}\n")
    if len(initial.lifebuoys) > 0 and lifebuoys_flag is False:
        print("********************************************************************")
        print("Pamiętaj, że możesz skorzystać z kół ratunkowych! Na tę chwilę masz do wyboru jeszcze:")
        for lifebuoy in initial.lifebuoys:
            print(f">>>>>>>>> {lifebuoy}")
        print("********************************************************************")
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
        print("\n********************************************************************")
        print("Wykorzystałeś już wszystkie koła ratunkowe! Musisz radzić sobie sam...")
        print("********************************************************************\n")