from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

year = input("Podaj rok urodzenia: ")
month = input("Podaj miesiąc urodzenia: ")
day = input("Podaj dzień urodzenia: ")

print(calculateAge(date(int(year), int(month), int(day))), "years")