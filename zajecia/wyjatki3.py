def funkcja():
    try:
        print("try")
        return "cokolwiek"
    except:
        # wykona się, kiedy wystąpi błąd
        print("except")
    else: #else się wykona kiedy nie weszliśmy w blok except
        print("else")
    finally: # on się wykona zawsze, nawet jak chcemy wcześniej wyjść z funkji poprzez return. Czy jest błąd, czy nie. Zamknięcie pliku, dostępu do bazy danych itp.
        print("finally")

funkcja() #finnaly i tak się wykona