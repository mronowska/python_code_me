import initial
import lifebuoys
import ask_and_answer

def main():
    initial.welcome()
    your_friend_tab = initial.who_is_your_friend()
    lifebuoys.friend_name = your_friend_tab[0]
    lifebuoys.friend_category = your_friend_tab[1]
    question_num = 0
    while question_num < 10:
        ask_and_answer.ask_question(initial.questions, question_num)
        question_num = question_num + 1

main()