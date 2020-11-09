import collections

krotka = ("Jan", "Kowalski", 170, 60, "Gdańsk")

Person = collections.namedtuple("Person", ["first_name", "last_name", "height", "weight", "city"]) #pierwsze to nazwa kolekcji (zwykle tak jak zmienna), potem pola

#w krotkach możemy po gwiazdce podawać argumenty po przecinku wygodnicko
jan_person = Person(*krotka)
print(jan_person)

