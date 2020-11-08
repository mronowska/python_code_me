import random

a, b, c = input("Podaj liczby: ").split(',')

for i in range(0, int(c)):
    print(random.randint(int(a), int(b)))