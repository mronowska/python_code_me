import datetime


class Employee:
    def __init__(self, name, surname, date_of_employment, base_salary=2137):
        self.name = name
        self.surame = surname
        self.date_of_employment = date_of_employment
        self.base_salary = base_salary

    def calculate_seniority(self):
        difference = datetime.date.today() - self.date_of_employment
        return difference.days

    def calculate_salary(self):
        salary = self.base_salary + 0.1 * self.base_salary * self.calculate_seniority() / 365
        return round(salary, 2)

class Manager(Employee):
    def __init__(self, name, surname, date_of_employment, manager_since, base_salary=4000):
        super().__init__(name, surname, date_of_employment, base_salary)
        self.manager_since = manager_since

    def calculate_salary(self):
        salary = 1.25 * self.base_salary + 0.1 * self.base_salary * self.calculate_seniority() / 365
        return round(salary, 2)

    def manager_for(self):
        difference = datetime.date.today() - self.manager_since
        return difference.days

wariacik = Employee("Morty", "Smith", datetime.date(2010, 6, 6))
print(f"Staż pracy {wariacik.name} {wariacik.surame} to {wariacik.calculate_seniority()} dni.")
print(f"{wariacik.name} {wariacik.surame} co miesiąc kasuje {wariacik.calculate_salary()} simoleonów.")

menago = Manager("Rick", "Sanchez", datetime.date(2012, 2, 13), datetime.date(2018, 11, 11))
print(f"Staż pracy {menago.name} {menago.surame} to {menago.calculate_seniority()} dni.")
print(f"{menago.name} {menago.surame} jest menadżerem od {menago.manager_for()} dni.")
print(f"{menago.name} {menago.surame} co miesiąc kasuje {menago.calculate_salary()} simoleonów.")