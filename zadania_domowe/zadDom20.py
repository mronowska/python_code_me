import csv

with open("przewoz_osob_gdynia.csv", encoding = "utf-8") as csvfile:
    reader = csv.reader(csvfile)

    list = []
    date = []

    for line in reader:
        list.append(line[0])
        date.append(line[1])

    #usuniecie nagłówków
    list.remove(list[0])
    date.remove(date[0])

    for i in range(0, len(list)):
        list[i] = float(list[i])

    index_max = list.index(max(list))
    index_min = list.index(min(list))

    print(f"Wartość najniższa {max(list)} tys. wystąpiła w {date[index_max]}")
    print(f"Wartość najniższa {min(list)} tys. wystąpiła w {date[index_min]}")

