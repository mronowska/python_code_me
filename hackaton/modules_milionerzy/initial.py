import random
import sys
import lifebuoys
import ask_and_answer

### questions - na przyszłość pobierać z pliku ###

questions = [
    ["Pyt. 1: Polskim odpowiednikiem baby shower jest:", "bociankowe", "prysznicowe", "500+", "becikowe", 0],
    ["Pyt. 2: W piosence Dwa plus Jeden pada propozycja: 'Chodź pomaluj mój świat...", "niech wygląda jak kwiat'", "mam już dość szarych krat'", "na żółto i na niebiesko'", "bo świat jest dziś pod kreską'", 2],
    ["Pyt. 3: Co jest tradycyjnym środkiem transportu amiszów?", "motorówka", "zaprzęg", "śnieżny skuter", "motocykl", 1],
    ["Pyt. 4: Pęd wyrosły z nieuszlachetnionej podkładki to:", "kot albo pies", "wilk albo dzik", "koń albo krowa", "baran albo kozioł", 1],
    ["Pyt. 5: Tytułowa wataha z serialu wyreżyserowanego m.in. przez Kasię Adamik to:", "wilcza rodzina", "rosyjscy szpiedzy", "strażnicy graniczni", "uchodźcy ze Wschodu", 2],
    ["Pyt. 6: Których bierek w bierkach jest najwięcej?", "wioseł", "bosaków", "trójzębów", "oszczepów", 3],
    ["Pyt. 7: W jakiej bitwie miał swój udział sławny w Polsce i Szkocji kapral niedźwiedź o imieniu Wojtek?", "pod Grunwaldem", "pod Wiedniem", "pod Monte Cassino", "o Anglię", 2],
    ["Pyt. 8: Aorta wychodzi z lewej komory serca, a kończy się:", "w prawej komorze", "w jamie brzusznej", "w płucach", "w mózgu", 1],
    ["Pyt. 9: Autor dwóch pozycji - 'Książki, którą napisałem, żeby mieć na dziwki i narkotyki' i 'Książki, którą napisałem, żeby mieć na odwyk' to:", "Marek Raczkowski", "Maciej Maleńczuk", "Kamil Durczok", "Witkacy", 3],
    ["Pyt. 10: Symbol waluty euro to stylizowana litera grecka. Która?", "beta", "heta", "eta", "epsilon", 3],
    ["Pyt. 11: Za 30 judaszowych srebrników arcykapłani kupili kawałek ziemi nazywany Polem Garncarza, który przeznaczyli na:", "plantację oliwek", "wybieg dla lwów", "cmentarz dla cudzoziemców", "targowisko", 2],
    ["Pyt. 12 ZA MILION!!!!: Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121", "12 321", "1 234 321", "111 111 111", "123 454 321", 1]
]

lifebuoys = [
    "telefon do przyjaciela",
    "pytanie do publiczności",
    "50/50"
]

def add_score(question_number):
    score = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
    return score[question_number]

def welcome():
    print("--------Witaj w grze Milionerzy!--------\n")
    print("---Odpowiedz poprawnie na 10 pytań i wygraj milion $$$$---\n")
    print("Dostępne koła ratunkowe: pytanie do publiczności, telefon do przyjaciela, 50/50!")