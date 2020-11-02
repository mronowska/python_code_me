def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def podziel(a, b):
    return a / b

def pomnoz(a, b):
    return a * b

def modulo(a, b):
    return a % b

def poteguj(a, b):
    return pow(a, b)

def enter_action():
    action = input("Jakie działanie chcesz wykonać?\n> dodaj,\n> odejmij\n> podziel\n> pomnoz\n> modulo\n> poteguj\n")
    return action

first_number = int(input("Podaj pierwszą liczbę: "))
sec_number = int(input("Podaj drugą liczbę: "))
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
    operations = operations[action]
    result = operations(first_number, sec_number)
    print(result)


