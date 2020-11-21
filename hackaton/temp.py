import csv

# def init():
#     with open('pytania.csv', 'r', encoding='utf-8') as questions_file:
#         questions_file = csv.reader(questions_file, delimiter=',')
#         for i in questions_file:
#             print(i[1])
#         return questions_file

#
# with open('pytania.csv', 'r', encoding='utf-8') as questions:
#     questions = list(csv.reader(questions, delimiter=','))
#
# def available_categories(questions_file):
#     categories = []  # deklaracja pustej listy
#     for category in questions:
#         categories.append(category[6])
#     return categories
#
# print(available_categories(questions))

# questions = [
#     ["Pyt. 1: Polskim odpowiednikiem baby shower jest:", "bociankowe", "prysznicowe", "500+", "becikowe", 0],
#     ["Pyt. 2: W piosence Dwa plus Jeden pada propozycja: 'Chodź pomaluj mój świat...", "niech wygląda jak kwiat'", "mam już dość szarych krat'", "na żółto i na niebiesko'", "bo świat jest dziś pod kreską'", 2],
#     ["Pyt. 3: Co jest tradycyjnym środkiem transportu amiszów?", "motorówka", "zaprzęg", "śnieżny skuter", "motocykl", 1],
#     ["Pyt. 4: Pęd wyrosły z nieuszlachetnionej podkładki to:", "kot albo pies", "wilk albo dzik", "koń albo krowa", "baran albo kozioł", 1],
#     ["Pyt. 5: Tytułowa wataha z serialu wyreżyserowanego m.in. przez Kasię Adamik to:", "wilcza rodzina", "rosyjscy szpiedzy", "strażnicy graniczni", "uchodźcy ze Wschodu", 2],
#     ["Pyt. 6: Których bierek w bierkach jest najwięcej?", "wioseł", "bosaków", "trójzębów", "oszczepów", 3],
#     ["Pyt. 7: W jakiej bitwie miał swój udział sławny w Polsce i Szkocji kapral niedźwiedź o imieniu Wojtek?", "pod Grunwaldem", "pod Wiedniem", "pod Monte Cassino", "o Anglię", 2],
#     ["Pyt. 8: Aorta wychodzi z lewej komory serca, a kończy się:", "w prawej komorze", "w jamie brzusznej", "w płucach", "w mózgu", 1],
#     ["Pyt. 9: Autor dwóch pozycji - 'Książki, którą napisałem, żeby mieć na dziwki i narkotyki' i 'Książki, którą napisałem, żeby mieć na odwyk' to:", "Marek Raczkowski", "Maciej Maleńczuk", "Kamil Durczok", "Witkacy", 3],
#     ["Pyt. 10: Symbol waluty euro to stylizowana litera grecka. Która?", "beta", "heta", "eta", "epsilon", 3],
#     ["Pyt. 11: Za 30 judaszowych srebrników arcykapłani kupili kawałek ziemi nazywany Polem Garncarza, który przeznaczyli na:", "plantację oliwek", "wybieg dla lwów", "cmentarz dla cudzoziemców", "targowisko", 2],
#     ["Pyt. 12 ZA MILION!!!!: Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121", "12 321", "1 234 321", "111 111 111", "123 454 321", 1]
# ]



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

print(f"{bcolors.HEADER}Warning: No active frommets remain. header?{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Warning: No active frommets remain. okblue?{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Warning: No active frommets remain. okgreen?{bcolors.ENDC}")
print(f"{bcolors.FAIL}Warning: No active frommets remain. fail?{bcolors.ENDC}")
print(f"{bcolors.ENDC}Warning: No active frommets remain. bold?{bcolors.ENDC}")
print(f"{bcolors.BOLD}Warning: No active frommets remain. okcyan?{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.BOLD}{bcolors.OKCYAN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")


