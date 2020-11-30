class Snake:
    type = "gad"

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def say_hello(self):
        self.name
        print(f"Hello, my name is {self.name}")

snake1 = Snake("Snaki", 100)
print(snake1.name, snake1.length, snake1.type)
snake2 = Snake("SSSSnake", 250)
print(snake2.name, snake2.length, snake2.type)
snake2.say_hello()