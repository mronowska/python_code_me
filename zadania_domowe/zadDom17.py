import random

def licz():
    dolny_zakres, gorny_zakres, ilosc_liczb = input("Podaj liczby w formacie 'dolny zakres, gorny zakres, ilosc liczb' np. '2, 13, 5': ").split(', ')

    for i in range(0, int(ilosc_liczb)):
        print(random.randint(int(dolny_zakres), int(gorny_zakres)))

licz()