import card as c
import random


class Deck():
    def __init__(self):
        self.deck = list()

        for suit in range(1, 4 + 1):
            for card in range(2, 5 + 1):
                self.deck.append(c.Card(card, suit))

        self.original_size = len(self.deck)  # This is just to make life easier on main.py lines 39 & 46

    def shuffl(self):
        random.shuffle(self.deck)

    # TEMPORARY
    def display(self):
        for item in self.deck:
            item.display()

    def deal(self):
        return self.deck.pop(-1)

    def size(self):
        return len(self.deck)
