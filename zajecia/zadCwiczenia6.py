def my_awesome_function(*args): #dowolna ilość argumentów, również 0/ krotka
    pass

def my_better_function(arg1, arg2="domyślna wartość"): #domyślne wartości wrzucamy na koniec
    pass

def my_better_function(arg2="domyślna wartość", *arg1): #domyślne wartości wrzucamy na koniec
    pass

def my_better_function2(**kwargs): #wymuszam na kodziarzu, aby podał wprost jakie arumenty przyjmuje/ słownik
    pass

my_better_function(a=1, b=2, c=3)
