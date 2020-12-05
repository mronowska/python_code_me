class Inverter:
    def __init__(self, text=""):
        self.text = text

    def enter_text(self):
        if self.text == "":
            self.text = input("Wprowadź napis: ")
        else:
            Exception()

    def print_text(self):
        print(self.text)

    def print_inverted_text(self):
        print(self.text[::-1])


text1 = Inverter()
text1.enter_text()
text1.print_inverted_text()
text1.enter_text()