import random
import sys
import initial
import ask_and_answer

def phone_call():
    print("\nDRYYNNN.... DRYNNN... HALO?! Tu Andrzej, tak, tak, widzę pytanie... Słuchaj, nie jestem pewien na sto procent, ale gdybym naprawdę... O jenki... Za takie pieniądze... Ziomek, miałbym tyle czipsów.. No nic... Słuchaj - ja bym wybrał odpowiedź B! Nie... A?... OSTATECZNIE C! Wybierz C!\n")
    index = initial.lifebuoys.index("telefon do przyjaciela")
    del initial.lifebuoys[index]

def audience():
    print("\nProszę Państwa... Proszę o głosy! <klik><klik><szumy><szumy> Ach tak, już widzę... Oczywiście. Oto wyniki publiczności:")
    answer_a = initial.random.randint(0, 100)
    answer_b = initial.random.randint(0, 100 - answer_a)
    answer_c = initial.random.randint(0, 100 - answer_a - answer_b)
    answer_d = 100 - answer_a - answer_b - answer_c
    print(f"Na odpowiedź A zagłosowało: {answer_a}% osób")
    print(f"Odpowiedź B: {answer_b}% osób")
    print(f"Z kolei na odpowiedź C: {answer_c}% osób")
    print(f"I wreszczie na odpowiedź D: {answer_d}% osób")
    print("Czy w czymś Ci to pomogło? Nakierowało? Teraz musisz wybrać!\n")
    index = initial.lifebuoys.index("pytanie do publiczności")
    del initial.lifebuoys[index]

def fifty_fifty(questions, question_number, right_answer_number):
    print("50/50 - to Twój wybór! Oto pozycje, które zostają (pozostałe dwie odrzucamy!)")
    first_option = right_answer_number
    sec_option = initial.random.randint(0, 4)
    print(sec_option)
    while first_option == sec_option:
        sec_option = initial.random.randint(0, 4)
    print(f"Pozostają opcje: {questions[question_number][first_option+1]} oraz {questions[question_number][sec_option+1]}! Pozostałe odrzucamy...")
    index = initial.lifebuoys.index("50/50")
    del initial.lifebuoys[index]

    def func_lifebuoys(questions, question_number):
        print(f"\nWybrałeś koło ratunkowe! Z którego chcesz skorzystać?")
        if initial.lifebuoys.count("telefon do przyjaciela") != 0:
            print("A. Telefon do przyjaciela")
        if initial.lifebuoys.count("pytanie do publiczności") != 0:
            print("B. Pytanie do publiczności")
        if initial.lifebuoys.count("50/50") != 0:
            print("C. 50/50")
        chosen_lifebuoy = input("Wybieram koło: ").upper()
        while chosen_lifebuoy != "A" and chosen_lifebuoy != "B" and chosen_lifebuoy != "C":
            print("Niepoprawna wartość... spróbuj jeszcze raz.")
            chosen_lifebuoy = input("Twój wybór: ").upper()
        if chosen_lifebuoy == "A":
            phone_call()
            ask_and_answer.analyze_answer(questions, question_number)
        if chosen_lifebuoy == "B":
            audience()
            ask_and_answer.analyze_answer(questions, question_number)
        if chosen_lifebuoy == "C":
            fifty_fifty(questions, question_number, questions[question_number][5])
            ask_and_answer.analyze_answer(questions, question_number)

def func_lifebuoys(questions, question_number):
    print(f"\nWybrałeś koło ratunkowe! Z którego chcesz skorzystać?")
    if initial.lifebuoys.count("telefon do przyjaciela") != 0:
        print("A. Telefon do przyjaciela")
    if initial.lifebuoys.count("pytanie do publiczności") != 0:
        print("B. Pytanie do publiczności")
    if initial.lifebuoys.count("50/50") != 0:
        print("C. 50/50")
    chosen_lifebuoy = input("Wybieram koło: ").upper()
    while chosen_lifebuoy != "A" and chosen_lifebuoy != "B" and chosen_lifebuoy != "C":
        print("Niepoprawna wartość... spróbuj jeszcze raz.")
        chosen_lifebuoy = input("Twój wybór: ").upper()
    if chosen_lifebuoy == "A":
        phone_call()
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "B":
        audience()
        ask_and_answer.analyze_answer(questions, question_number)
    if chosen_lifebuoy == "C":
        fifty_fifty(questions, question_number, questions[question_number][5])
        ask_and_answer.analyze_answer(questions, question_number)