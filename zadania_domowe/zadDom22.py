import collections

def pobierz_dane():
    sentence = input("Podaj jakieś długie zdanie: ")
    return sentence

def odczytaj_plik():
    filepath = "pan_tadeusz.txt"
    f = open(filepath, "r", encoding="utf-8")
    return f.read()

def policz_litery(sentence, num):
    c = collections.Counter(sentence)
    print(f"Najpopularniejsze znaki to: {c.most_common(num)}")

tekst = pobierz_dane()
policz_litery(tekst, len(tekst))
policz_litery(odczytaj_plik(), 4)