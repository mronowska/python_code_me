def dodaj(a, b):
    return int(a) + int(b)

def odejmij(a, b):
    return int(a) - int(b)

def podziel(a, b):
    return int(a) / int(b)

def pomnoz(a, b):
    return int(a) * int(b)

def modulo(a, b):
    return int(a) % int(b)

def poteguj(a, b):
    return pow(int(a), int(b))

def enter_action():
    action = input("Jakie działanie chcesz wykonać?\n> dodaj,\n> odejmij\n> podziel\n> pomnoz\n> modulo\n> poteguj\n")
    return action

first_number, sec_number = input("Podaj dwie liczby (oddziel spacją): ").split()

print(f"Pierwsza liczba to {first_number}, a druga to {sec_number}.")

list = ["dodaj", "odejmij", "pomnoz", "podziel", "modulo", "poteguj"]

action = enter_action()
while action not in list:
    print("Niepoprawna wartość... Spróbuj jeszcze raz.")
    action = enter_action()

# if action == "dodaj":
#     print(dodaj(first_number, sec_number))
# elif action == "odejmij":
#     print(odejmij(first_number, sec_number))
# elif action == "podziel":
#     print(podziel(first_number, sec_number))
# elif action == "pomnoz":
#     print(pomnoz(first_number, sec_number))
# elif action == "modulo":
#     print(modulo(first_number, sec_number))
# elif action == "poteguj":
#     print(poteguj(first_number, sec_number))


## pythonowskie SWITCH - CASE
operations = {
    "dodaj": dodaj,
    "odejmij": odejmij,
    "pomnoz": pomnoz,
    "podziel": podziel,
    "modulo": modulo,
    "poteguj": poteguj
}

if action in operations:
    operation = operations[action]
    result = operation(first_number, sec_number)
    print(result)


