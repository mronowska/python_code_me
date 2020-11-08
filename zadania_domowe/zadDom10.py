wynik = int(input("Podaj swój wynik w %: "))

if wynik < 100 and wynik > 91:
    print("5 - super")
elif wynik < 90 and wynik > 75:
    print("4 - oks")
elif wynik < 74 and wynik > 51:
    print("3 - średnio")
elif wynik < 50 and wynik > 30:
    print("2 - słabo")
else:
    print("Nie zdałeś.")