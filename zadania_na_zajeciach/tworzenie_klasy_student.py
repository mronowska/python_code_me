class Student:
    def __init__(self, imie, nazwisko, kierunek, uczelnia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.uczelnia = uczelnia
        self.kierunek = kierunek

    def oblicz_srednia(self):
        oceny = [1, 3, 4, 6, 3, 5, 4]
        suma = 0

        for ocena in oceny:
            suma = suma + ocena

        srednia = suma / len(oceny)
        return round(srednia, 2)

    def poprawny_indeks(self, indeks):
        if len(indeks) > 3:
            return True
        else:
            return False

    @classmethod
    def student_IT_PG(cls, imie, nazwisko):
        it_student = cls(imie, nazwisko, "informatyka", "PG")
        return it_student

    #zwracanie konktetnego studenta
    def __str__(self):
        return f"Student {self.imie}, {self.kierunek}"


student1 = Student("Andrzej", "Andrzejowski", "matematyka", "UG")
print(student1.oblicz_srednia())

student2 = Student.student_IT_PG("Alojzy", "Krzawiasty")
print(student2)