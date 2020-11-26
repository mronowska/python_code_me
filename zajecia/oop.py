class Prostokat:
    def __init__(self, dl, szer, x = "0", y="0"):
        self.dl = dl
        self.szer = szer
        self.x = x
        self.y = y

prostokat1 = Prostokat(10, 20, 11, 11)
prostokat2 = Prostokat(21, 37)
prostokat3 = Prostokat(5,4)

def drukuj(prostokat, nr):
    print(f"Prostokąt nr {nr}.")
    print(f"Długość: {prostokat.dl}")
    print(f"Szerokość: {prostokat.szer}")
    print(f"X: {prostokat.x}")
    print(f"Y: {prostokat.y}")
    print(f"Pole: {int(prostokat.dl) * int(prostokat.szer)}\n")

drukuj(prostokat1, 1)
drukuj(prostokat2, 2)
drukuj(prostokat3, 3)
