#generowanie hasel

import random

pass_len = int(input("Podaj długość hasła (min. 4 znaki): "))

while int(pass_len) < 4:
    print("Za krótkie ziomek... Zrób porządne hasło, daj 4 lub więcej")
    pass_len = input("Podaj długość hasła (min. 4 znaki): ")

def random_index(char):
    return random.randint(0, len(char))

def password(pass_len):
    your_password_list = []
    symbols = '!@#$%^&*()'
    lowercase = 'qwertyuioplkjhgfdsazxcvbnm'
    uppercase = lowercase.upper()
    numbers = '1234567890'

    options_list = [symbols, lowercase, uppercase, numbers]

    pass_list_required = [symbols[random_index(symbols)], lowercase[random_index(lowercase)], uppercase[random_index(uppercase)], numbers[random_index(numbers)]]

    supplement_options = []

    if pass_len > 4:
        temp = pass_len - 4
        for i in range(temp, pass_len):
            random_option_number = random.randint(0, 3)
            supplement_options.append(options_list[random_option_number])
            for x in supplement_options:
                if x == symbols:
                    your_password_list.append(symbols[random_index(symbols)])
                if x == lowercase:
                    your_password_list.append(lowercase[random_index(lowercase)])
                if x == uppercase:
                    your_password_list.append(uppercase[random_index(uppercase)])
                if x == numbers:
                    your_password_list.append(numbers[random_index(numbers)])
    print(f"Pass list = {your_password_list}")
    your_password = your_password_list + pass_list_required
    str = ""
    for ele in your_password:
        str += ele

    return str

print(password(pass_len))
#print(listToString(password(pass_len)))
