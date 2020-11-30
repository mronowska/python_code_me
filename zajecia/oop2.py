class Snake:
    type = "gad"

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def say_hello(self):
        self.name
        print(f"Hello, my name is {self.name}")

    #etykietka dla wyswietlania objektu dla użytkownika końcowego
    def __str__(self):
         return f"Etykieta dla użytkownika: {self.name}"

    #dla programistów, żeby widzieć w debugowaniu co się dzieje
    def __repr__(self):
        return f"Reprezentacja obiektu {self.name}"

snake1 = Snake("Snaki", 100)
print(snake1.name, snake1.length, snake1.type)
snake2 = Snake("SSSSnake", 250)
print(snake2.name, snake2.length, snake2.type)
snake2.say_hello()
print(snake1)
print(snake2)

snakes = [snake1, snake2]
print(snakes)