#generowanie hasel

import random

def random_index(char:str):
    return random.randint(0, len(char) - 1)

def password(pass_len):
    your_password_list = []
    symbols = '!@#$%^&*()'
    lowercase = 'qwertyuioplkjhgfdsazxcvbnm'
    uppercase = lowercase.upper()
    numbers = '1234567890'

    options_list = [symbols, lowercase, uppercase, numbers]

    pass_list_required = [symbols[random_index(symbols)], lowercase[random_index(lowercase)], uppercase[random_index(uppercase)], numbers[random_index(numbers)]]

    supplement_options = []

    if int(pass_len) > 4:
        temp = int(pass_len) - 4
        for i in range(temp):
            random_option_number = random.randint(0, 3) #losuj numer indeksu od 0 do 3
            supplement_options.append(options_list[random_option_number])

        for x in supplement_options:
            if x == symbols:
                your_password_list.append(symbols[random_index(symbols)])
            elif x == lowercase:
                your_password_list.append(lowercase[random_index(lowercase)])
            elif x == uppercase:
                your_password_list.append(uppercase[random_index(uppercase)])
            elif x == numbers:
                your_password_list.append(numbers[random_index(numbers)])

    your_password = []
    your_password.extend(your_password_list)
    your_password.extend(pass_list_required)

    final_password = ""
    for ele in your_password:
        final_password += ele

    return final_password

def main():
    pass_len = input("Podaj długość hasła (min. 4 znaki): ")

    while int(pass_len) < 4:
        print("Za krótkie ziomek... Zrób porządne hasło, daj 4 lub więcej")
        pass_len = input("Podaj długość hasła (min. 4 znaki): ")

    print(f"Oto Twoje hasło: {password(pass_len)}")

main()
