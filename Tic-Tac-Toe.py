import os

board = [i for i in range(1, 10)]
turn = True
new_board = []

def print_board(lst):
    for i in range(11):
        if i == 1:
            print(f" {lst[0]} S {lst[1]} S {lst[2]} ")
            continue
        elif i == 5:
            print(f" {lst[3]} S {lst[4]} S {lst[5]} ")
            continue
        elif i == 9:
            print(f" {lst[6]} S {lst[7]} S {lst[8]} ")
            continue
        elif i % 2 == 0:
            print("   S   S   ")
            continue
        else:
            print("SSSSSSSSSSS")


def grab_input(turn):
    while True:
        try:
            in_ = int(input("ENTER THE CELL NUMBER ({}): ".format("X" if turn else "O")))
            if in_ > 0 and in_ < 10:
                break
        except ValueError:
            print("NOT A NUMBER, PLEASE TRY AGAIN!")

    return in_


def update_board(board, num, turn):
    os.system('cls')
    board = board[::]
    if type(board[num - 1]) == int:
        # board[num-1] = "X" if turn else "O"
        if turn:
            board[num - 1] = "X"
        else:
            board[num - 1] = "O"
    return board


def check_for_winner(board):
    # check for horizontal:
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True

    # check for vertical
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True

    # check for diagnal
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True


os.system('cls')

while True:
    print("***************WELCOME TO TIC-TAC-TOE SAGUIII***************")
    print_board(board)
    i = grab_input(turn)
    new_board = update_board(board, i, turn)

    if new_board != board:
        if check_for_winner(new_board):
            print_board(new_board)
            print("CONGRATULATIONS '{}', YOU JUST WON!!!".format("Mr. X" if turn else "Mr. O"))
            if input("NEW GAME? (y/n)") == "y":
                board = [i for i in range(1, 10)]
                os.system('cls')
                continue
            print("THANKS FOR PLAYING!!")
            break
        turn = not turn
        board = new_board

