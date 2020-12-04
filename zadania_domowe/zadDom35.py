import datetime
class Book:
    def __init__(self, title, author, year, genre, pages, book_description):
        today = datetime.date.today()
        self.title = title
        self.author = author
        if year > today.year:
            raise ValueError(f"Release year can't be greater than {today.year}")
        self.year = year
        self.genre = genre
        if pages < 0:
            raise ValueError(f"Pages must be a number greater than 0")
        self.pages = pages
        self.book_description = book_description

    def describe_book(self):
        print(self.book_description)

    def update_genre(self):
        new_genre = input(f"Wprowadź nowy gatunek książki {self.title}: ")
        self.genre = new_genre



b1 = Book("Harry Potter", "J.K. Rowling", 2001, "fantasy", 300, "Bardzo fajna, najlepsza książka, są czarodzieje i profesor Snape")

b2 = Book("Wiedźmin", "Andrzej Sapkowski", 2010, "fantasy", 630, "Dla nerdów, ale 3 Wiedźmin 3 najlepszy")

b1.describe_book()
b2.describe_book()
b1.update_genre()
