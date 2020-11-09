#roznice w pensjach

def salary_differences(salary_1, salary_2, salary_3):
    salary = [int(salary_1), int(salary_2), int(salary_3)]
    salary_sorted = sorted(salary)
    return salary_sorted[2] - salary_sorted[0]

def main():
    salary_1 = input("Podaj pierwszą pensję (w PLN): ")
    salary_2 = input("Podaj drugą pensję (w PLN): ")
    salary_3 = input("Podaj trzecią pensję (w PLN): ")

    return print(f"Różnica pomiędzy najwyższą i najniższą pensją to {salary_differences(salary_1, salary_2, salary_3)} PLN")

main()

#Jak zmienisz program, żeby została zwrócona różnica między środkową a najniższą pensją?
#Wystarczy zamiast salary_sorted[2] podstawić salary_sorted[1] w odejmowaniu

