import random


# count = 0

class Player():
    def __init__(self, n=""):
        # global count
        # count += 1
        # check if name is empty if it is assign a number check if name is emty if it is assign a number
        # self.name = ("Player " + count) if len(n) < 1 else n

        self.name = n
        self.hand = list()

    def recieve_card(self, card):
        # print(f"CARD WAS GIVEN TO {self.name}")
        self.hand.insert(0, card)

    def remove_card(self):  # FICX THIS ASAP
        if len(self.hand) > 0:
            c = self.hand.pop(-1)
            return c
        return False

    def draw_3cards(self):
        pass

    def hand_size(self):
        return len(self.hand)

    def shuffl_hand(self):
        random.shuffle(self.hand)

    def take_all_cards(self, p):
        for c in p.hand:
            self.hand.append(c)
        p.hand.clear()
