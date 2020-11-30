import random

class CardsDeck:
    def __init__(self):
        colors = ["clubs", "spades", "hearts", "diamonds"]
        figures = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        all_cards = []
        for color in colors:
            for figure in figures:
                all_cards.append(f"{figure} {color}")
        self.cards = all_cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def give_me_card(self):
        last_card = self.cards.pop()
        return last_card


deck1 = CardsDeck()
print(deck1.cards)

deck1.shuffle_deck()
print(deck1.cards)

#podaj ostatnią kartę z potasowanych
print(deck1.give_me_card())