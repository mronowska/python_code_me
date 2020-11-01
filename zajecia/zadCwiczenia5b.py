#Zadanie 2

cena_za_litr = 4.99
spalanie = 5.7

cena_trasy = float(input("Ile jesteś w stanie wydać na ten wyskok (w zł)? "))
km_trasy = float(input("Ile km chcesz przejechać? "))


spalanie_na_trase = km_trasy * spalanie / 100
koszt_trasy = spalanie_na_trase * cena_za_litr

if cena_trasy >= koszt_trasy:
    print("Możesz jechać.")
else:
    print("Za drogo, odpuść...")