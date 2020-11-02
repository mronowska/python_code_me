## zadanie 15 biuro podrozy

Canada = {
    "flight" : 2137,
    "car" : 150,
    "hotel": 100
}

Iceland = {
    "flight" : 188,
    "car" : 250,
    "hotel": 240
}

Norway = {
    "flight" : 18,
    "car" : 100,
    "hotel": 123
}

def main():
    list_of_destinations = ["Kanada", "Islandia", "Norwegia"]
    print("Siemano niezłe wdziano")
    print("Masz do wyboru aż 3 super lokalizacje na wyjazd! Kanada, Islandia, Norwegia.")
    destinatnion = input("Gdzie byś chciał/a pojechać? Wpisz: ")

    while destinatnion not in list_of_destinations:
        print("Mówiłam, żebyś wybrał/a z tych trzech... Spróbuj ponownie!")
        destinatnion = input("Gdzie byś chciał/a pojechać? Wpisz: ")

    days = int(input("Ile dób chcesz tam spędzić? Wpisz: "))

    if destinatnion == "Kanada":
        print(f"Na loty wydasz {Canada['flight']} PLN")
        print(f"Na auto wydasz {Canada['car'] * days} PLN")
        print(f"Na auto wydasz {Canada['hotel'] * days} PLN")
    elif destinatnion == "Islandia":
        print(f"Na loty wydasz {Iceland['flight']} PLN")
        print(f"Na auto wydasz {Iceland['car'] * days} PLN")
        print(f"Na auto wydasz {Iceland['hotel'] * days} PLN")
    elif destinatnion == "Norwegia":
        print(f"Na loty wydasz {Norway['flight']} PLN")
        print(f"Na auto wydasz {Norway['car'] * days} PLN")
        print(f"Na auto wydasz {Norway['hotel'] * days} PLN")

main()
