import math


class Card():
    def __init__(self, value, suit):
        self.symbol_dic = {0: " ", 14: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                           10: "Jack", 11: "King", 12: "Queen", 13: "King"}
        self.suit_dic = {0: " ", 1: "♣", 2: "♦", 3: "♠", 4: "♥"}
        self.visible = False

        # INTS
        self.value = value
        self.width = 7
        self.length = 11

        # STRINGS
        self.suit = self.suit_dic[suit]

    def display(self):
    # THIS CODE IS WHAT WAS USED BEFORE I ADDED A SCREEN LIST TO MY MAIN.PY
    # if self.visible:
    #     # print(f"{self.symbol_dic[self.value]} of {self.suit}")
    #     # pint card base
    #     print(" --------------------- ")
    #     print(f"| {self.suit[0]}                   |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print(f"|         {self.symbol_dic[self.value][0]}           |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print(f"|                   {self.suit[0]} |")
    #     print(" --------------------- ")
    #
    # else:
    #     # print("**THIS CARD IS NOT VISIBLE**")
    #     print(" --------------------- ")
    #     print("| ?                   |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|         ???         |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                     |")
    #     print("|                   ? |")
    #     print(" --------------------- ")
        pass

    # def __str__(self):
    #     return f"{self.symbol_dic[self.value]} of {self.suit}"

    # this will do all the calculations and modification on the display list of cards we will be printing on the screen
    def add_to_display(self, lis):
        if self.visible:
            if not lis:
                for line in range(self.length):
                    if line == 0 or line == self.length-1:
                        lis.append([[" -------"], ["  "], ["\n"]])
                    else:
                        if line == 1:
                            lis.append([[f"| {self.suit}     |"], [" "], ["\n"]])
                        elif line == math.ceil(int(self.length / 2)):
                            lis.append([[f"|   {self.symbol_dic[self.value][0]}   |"], [" "], ["\n"]])
                        elif line == self.length - 2:
                            lis.append([[f"|     {self.suit} |"], [" "], ["\n"]])
                        else:
                            lis.append([[f"|       |"], [" "], ["\n"]])

            else:
                for line in range(self.length):
                    if line == 0 or line == self.length - 1:
                        lis[line][-1:-1] = [[" -------"]]
                        lis[line][-1:-1] = [["  "]]
                    else:
                        if line == 1:
                            lis[line][-1:-1] = [[f"| {self.suit}     |"]]
                            lis[line][-1:-1] = [[" "]]
                        elif line == math.ceil(int(self.length / 2)):
                            lis[line][-1:-1] = [[f"|   {self.symbol_dic[self.value][0]}   |"]]
                            lis[line][-1:-1] = [[" "]]
                        elif line == self.length - 2:
                            lis[line][-1:-1] = [[f"|     {self.suit} |"]]
                            lis[line][-1:-1] = [" "]
                        else:
                            # if line != self.length -1
                            lis[line][-1:-1] = [[f"|       |"]]
                            lis[line][-1:-1] = [[" "]]

        else:
            for line in range(self.length):
                if line == 0 or line == self.length - 1:
                    lis[line][-1:-1] = [[" -------"]]
                    lis[line][-1:-1] = [["  "]]
                else:
                    if line == 1:
                        lis[line][-1:-1] = [[f"| ?     |"]]
                        lis[line][-1:-1] = [[" "]]
                    elif line == math.ceil(int(self.length / 2)):
                        lis[line][-1:-1] = [[f"|  ???  |"]]
                        lis[line][-1:-1] = [[" "]]
                    elif line == self.length - 2:
                        lis[line][-1:-1] = [[f"|     ? |"]]
                        lis[line][-1:-1] = [" "]
                    else:
                        # if line != self.length -1
                        lis[line][-1:-1] = [[f"|       |"]]
                        lis[line][-1:-1] = [[" "]]