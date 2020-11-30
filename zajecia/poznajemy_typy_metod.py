class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def describe_company(self):
        print(f"Company {self.name} has {len(self.employess)} employees")

    def add_employee(self, employee_name):
        self.employees.append(employee_name)


    @staticmethod    #dekorator metody statycznej, może być na obiekcie bądź klasie
    def moja_metoda_statyczna(self):
        print("Cześć")

    @classmethod #może być tylko na klasie
    def moja_metoda_klasowa(cls):
        return ""

    @classmethod
    def create_finance_company(cls, name):
        company = cls(name, "Finance")

    @classmethod
    def create_it_company(cls, name):
        company = cls(name, "IT")

company = Company("ViaRial", "IT")

c1 = Company.create_it_company("Adva")
c2 = company.create_finance_company("PKO")

print(c1)