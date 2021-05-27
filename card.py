class Card():
    def __init__(self, value, suit):
        self.symbol_dic = {0: " ", 14: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "Jack", 11: "King", 12: "Queen", 13: "King"}
        self.suit_dic = {0: " ", 1: "♣", 2: "♦", 3: "♠", 4: "♥"}
        self.visible = False

        #INTS
        self.value = value

        # STRINGS
        self.suit = self.suit_dic[suit]


    def display(self):
        if self.visible:
            # print(f"{self.symbol_dic[self.value]} of {self.suit}")
            # pint card base
            print(" --------------------- ")
            print(f"| {self.suit[0]}                   |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print(f"|         {self.symbol_dic[self.value][0]}           |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print(f"|                   {self.suit[0]} |")
            print(" --------------------- ")

        else:
            # print("**THIS CARD IS NOT VISIBLE**")
            print(" --------------------- ")
            print("| ?                   |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|         ???         |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                     |")
            print("|                   ? |")
            print(" --------------------- ")

    # def __str__(self):
    #     return f"{self.symbol_dic[self.value]} of {self.suit}"