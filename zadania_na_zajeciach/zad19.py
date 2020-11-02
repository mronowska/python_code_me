def main():
    numbers = []
    numbers = input("Podaj liczby: ")
    numbers = numbers.split(", ")
    numbers = [int(num) for num in numbers] # tworze liste int numbers, która jest pusta i dla dodaj po kolei elementy w formie int
    ## to powyżej to to samo co:
    # int_numbers = []
    # for num in numbers:
    #   int_numbers.append(int(num))
    print(max(numbers))


main()