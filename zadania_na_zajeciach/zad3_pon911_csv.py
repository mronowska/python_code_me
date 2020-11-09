import collections
import csv

Actor = collections.namedtuple("Actor", ["index", "year", "age", "name", "movie"])

#otworz plik csv

with open("oscar_age_male.csv", encoding = "utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) #czytanie 1 linijki?

#przechowanie danych z wiersza jako namedtuple

    for line in reader:
        actor = Actor(*line)
        print(f"{actor.name} has won in {actor.year} with {actor.movie}")
