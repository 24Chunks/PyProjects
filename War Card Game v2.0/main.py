import player
import deck
import os  # WILL DO SUM WITH THIS LATER

# this is what we will be displaying in our screen
screen = list()


def draw3_cards(p1, p2, t):
    for i in range(1, 4):
        t.append(p1.remove_card())
        t[i * -1].add_to_display(screen)

    for i in range(1, 4):
        t.append(p2.remove_card())
        t[i * -1].add_to_display(screen)


def compare(c1, c2):
    if c1.value > c2.value:
        return 1
    elif c1.value < c2.value:
        return 2
    else:
        return -1


def get_input(p):
    return input(f"{p.name}, Whenever you are ready PRESS (ENTER)/(Q): ")


def determine_winner(p1, p2, d):
    if p1.hand_size() == d.original_size:

        print(f"Congrats!! {p1.name}, You have Won!!")
        print(f"{p1.name} HAND SIZE {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
        print(f"{p2.name} HAND SIZE {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))

        return True
    elif p2.hand_size() == d.original_size:
        print(f"Congrats!! {p2.name}, You have Won!!")

        print(f"{p1.name} HAND SIZE  {p1.hand_size()}" + (" :'(" if p1.hand_size() == 0 else ""))
        print(f"{p2.name} HAND SIZE  {p2.hand_size()}" + (" :'(" if p2.hand_size() == 0 else ""))

        return True
    return False


def render_screen(sc, p1, p2, temp_p, c):
    for line in sc:
        for p in line:
            print("".join(p), end="")

    if temp_p and c:
        print()
        print(f"{temp_p.name} JUST GOT ADDED {c} CARDS!")
        print()
    # print(f"Succesfully Added {n} cards to {p}!") THIS FEATURE WILL BE ADDED LATER
    print(f"{p1.name}'s Hand Size: ", p1.hand_size())
    print(f"{p2.name}'s' Hand Size: ", p2.hand_size())
    print()


def get_player_input(p, table):
    inpt = get_input(p)
    while inpt:
        if inpt.lower() == "q":
            return -1
        else:
            inpt = get_input(p)
    else:
        table.append(p.remove_card())
        if table[-1] != type(bool):
            table[-1].visible = True
            table[-1].add_to_display(screen)
        else:
            table.pop(-1)


def Game():
    d = deck.Deck()
    d.shuffl()

    table = list()

    p1 = player.Player("Player 1")
    p2 = player.Player("Player 2")

    temp_p = player.Player()
    cards_added_counter = 0

    # c__1 = crd.Card(2, 1)

    # distribute cards to players
    for index in range(d.size()):
        if index % 2 == 0:
            p1.recieve_card(d.deal())
        else:
            p2.recieve_card(d.deal())

    # p1.hand[-1] = c__1
    # p2.hand[-1] = c__1

    os.system("cls")
    print("-------------WELCOME TO WAR CARD GAME by L0sD4B0S5 v2.0-------------")
    print("ATTENTION: PLEASE ENTER FULL SCREEN ON YOUR COMMAND CONSOLE BEFORE STARTING THE GAME")
    in_ = str(input("Enter Player 1 Name: "))

    if in_:
        p1.name = in_
    in_ = str(input("Enter Player 2 Name: "))
    if in_:
        p2.name = in_

    print(f"{p1.name} Starting Hand Size: ", p1.hand_size())
    print(f"{p2.name} Starting Hand Size: ", p2.hand_size())
    print()

    while not determine_winner(p1, p2, d):

        if get_player_input(p1, table) == -1:
            break
        if get_player_input(p2, table) == -1:
            break
        os.system("cls")
        print("-------------WELCOME TO WAR CARD GAME by L0sD4B0S5 v2.0-------------")

        if compare(table[-2], table[-1]) == 1:
            # print(f"Cards added: {len(table)}")
            cards_added_counter = 0
            for c in table:
                cards_added_counter += 1
                c.visible = False
                p1.recieve_card(c)

            temp_p = p1


        elif compare(table[-2], table[-1]) == 2:
            # print(f"Cards added: {len(table)}")
            cards_added_counter = 0
            for c in table:
                cards_added_counter += 1
                c.visible = False
                p2.recieve_card(c)
            temp_p = p2

        # compare two cards
        # IF THEY EQUAL
        elif compare(table[-1], table[-2]) == -1:
            # check if both players still have more then 3 cards, if so keep playing
            if p1.hand_size() > 3 and p2.hand_size() > 3:
                draw3_cards(p1, p2, table)
                render_screen(screen, p1, p2, None, None)
                continue

            # if someone has less then 3 cards determine winner
            else:
                render_screen(screen, p1, p2, None, None)
                if p2.hand_size() < 4:
                    p1.take_all_cards(p2)

                    # grab cards left on table
                    for c in table:
                        p1.recieve_card(c)
                    determine_winner(p1, p2, d)
                    break
                else:
                    p2.take_all_cards(p1)

                    # grab cards left on table
                    for c in table:
                        p2.recieve_card(c)

                    determine_winner(p1, p2, d)
                    break
                # CHECK WHIS DA WINNA!!!
                # if check_for_dub(p1, p2) == -1:
                #     break

        # clears table after distributing cards
        # print(screen)
        render_screen(screen, p1, p2, temp_p, cards_added_counter)
        screen.clear()
        table.clear()
        p1.shuffl_hand()
        p2.shuffl_hand()


Game()
