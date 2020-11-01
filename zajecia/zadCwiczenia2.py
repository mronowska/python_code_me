a = 100.5
b = 21.37

print(round(a+b))
print(type(a)) #typ w formacie <class 'float'>

##działania matematyczne

print(a // b) #dzielenie bez reszty
print(a % 2) #modulo - np. czy liczba jest parzysta
print(a ** 3) #potęgowanie
print(divmod(5, 2)) #(5 // 2, 5 % 2)

print(0.1 + 0.2) #haczyk - jest ciut większe niż 0.3... :( Dokumentacja Python - szczegóły

import decimal
var = print(decimal.Decimal('0.1') + decimal.Decimal('0.1') == decimal.Decimal('0.3'))

##logika

print(5 is 5) #life is life :D - true - sprawdza też miejsca w pamięci, konkretne wartości itd

print(bool(''))

