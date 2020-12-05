class Rectangle:
    def __init__(self, length, width, coord=(0, 0)):
        self.length = length
        self.width = width
        self.coord = coord
        self.pole = length * width

    def calculate_area(self):
        return self.length * self.width

    @property
    def dynamiczne_pole(self):
        return self.length * self.width

def describe_rectangle(rect):
    print(rect.length, rect.width, rect.coord)

def calculate_area(rect):
    return rect.length * rect.width

r1 = Rectangle(10, 12)
r2 = Rectangle(5, 8, (10, 10))
r3 = Rectangle(24, 10)
print(r1.pole)
print(r1.dynamiczne_pole)
r1.length = 15
print(r1.pole)
print(r1.dynamiczne_pole)

describe_rectangle(r1)
describe_rectangle(r2)
describe_rectangle(r3)

print(calculate_area(r1))
print(calculate_area(r2))
print(calculate_area(r3))

print(r1.calculate_area())