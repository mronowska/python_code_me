import initial
import lifebuoys
import ask_and_answer
import phone_call
import friend

def main():
    initial.welcome()
    your_friend_tab = friend.who_is_your_friend()
    phone_call.friend_name = your_friend_tab[0]
    phone_call.friend_category = your_friend_tab[1]
    question_num = 0
    while question_num < 10:
        ask_and_answer.ask_question(initial.questions, question_num)
        question_num = question_num + 1

main()