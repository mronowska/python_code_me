import random

def read_file():
    filepath = "ich_troje_powiedz.txt"
    f = open(filepath, "r", encoding="utf-8")
    return f

def create_tab():
    tab = []
    for line in read_file():
        tab.append(line)
    return tab

index = random.randint(0, len(create_tab()))
print(create_tab()[index])