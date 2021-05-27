import player
import deck
import os # WILL DO SUM WITH THIS LATER


# deck.display()

def draw_cards(p1, p2, t):

    for i in range(1, 4):
        t.append(p1.remove_card())
        t[i * -1].display()

    print()
    print()
    print()
    print()
    print()

    for i in range(1, 4):
        t.append(p2.remove_card())
        t[i * -1].display()


def compare(c1, c2):
    if c1.value > c2.value:
        return 1
    elif c1.value < c2.value:
        return 2
    else:
        return -1


def get_input(p):
    return input(f"Player {p.name}: are you ready? (y/n)")


def check_for_dub(p1, p2, d):
    if p1.hand_size() == d.original_size:

        print(f"Congrats!! {p1.name}, You have Won!!")
        print(f"{p1.name} HAND SIZE {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
        print(f"{p2.name} HAND SIZE {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))

        return -1
    elif p2.hand_size() == d.original_size:
        print(f"Congrats!! {p2.name}, You have Won!!")

        print(f"{p1.name} HAND SIZE  {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
        print(f"{p2.name} HAND SIZE  {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))

        return -1
    return 0

def Game():

    d = deck.Deck()
    d.shuffl()

    table = list()

    p1 = player.Player("Sagui")
    p2 = player.Player("Carlos")

    # c__1 = crd.Card(2, 1)

    # distribute cards to players
    for index in range(d.size()):
        if index % 2 == 0:
            p1.recieve_card(d.deal())
        else:
            p2.recieve_card(d.deal())

    # p1.hand[-1] = c__1
    # p2.hand[-1] = c__1

    while True:

        print(f"Player {p1.name} Hand Size: ", p1.hand_size())
        print(f"Player {p2.name} hand Size: ", p2.hand_size())
        print()

        if check_for_dub(p1, p2, d) == -1:
            break

        if not get_input(p1):
            #print("P1: ", end="")##################
            table.append(p1.remove_card())
            if table[-1] is not type(bool):
                table[-1].visible = True
                table[-1].display()
            else :
                table.pop(-1)

        if not get_input(p2):
            #print("P1: ", end="") ##################
            table.append(p2.remove_card())
            if table[-1] is not type(bool):
                table[-1].visible = True
                table[-1].display()
            else :
                table.pop(-1)

        if compare(table[-2], table[-1]) == 1:
            # print(f"Cards added: {len(table)}")
            for c in table:
                c.visible = False
                p1.recieve_card(c)

        elif compare(table[-2], table[-1]) == 2:
            # print(f"Cards added: {len(table)}")
            for c in table:
                c.visible = False
                p2.recieve_card(c)

        # compare two cards
        # IF THEY EQUAL
        elif compare(table[-1], table[-2]) == -1:
            if p1.hand_size() > 3 and p2.hand_size() > 3:
                draw_cards(p1, p2, table)
                continue
            else:
                if p2.hand_size() < 4:
                    p1.take_all_cards(p2)

                    # garbcard left on table
                    for c in table:
                        p1.recieve_card(c)


                    print(f"{p1.name} HAND SIZE {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
                    print(f"{p2.name} HAND SIZE {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))
                    break
                else:
                    p2.take_all_cards(p1)

                    #garbcard left on table
                    for c in table:
                        p2.recieve_card(c)

                    print(f"{p1.name} HAND SIZE {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
                    print(f"{p2.name} HAND SIZE {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))
                    break
                #CHECK WHIS DA WINNA!!!
                # if check_for_dub(p1, p2) == -1:
                #     break


        # clears table after distributing cards
        table.clear()
        p1.shuffl_hand()
        p2.shuffl_hand()

Game()
