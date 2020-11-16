import initial
import lifebuoys
import ask_and_answer

def play():
    initial.welcome()
    question_num = 0
    while question_num < 10:
        ask_and_answer.ask_question(initial.questions, question_num)
        question_num = question_num + 1

play()