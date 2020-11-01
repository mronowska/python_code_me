import decimal

year = 2020
age = input("Rok urodzenia: ")
print(f"Wygląda na to, że masz {year - decimal.Decimal(age)} lat! Nieźle.")

## inaczej - przez int
print(f"\nA przez int tak: Wygląda na to, że masz {year - int(age)} lat! Nieźle. :D")
