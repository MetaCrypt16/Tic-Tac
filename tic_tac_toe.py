import random


def print_board(board):
    for row in range(3):  # loop over 3 rows
        # using f strings formatted strings
        print(f"{board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]}")
        if row < 2:  # to seperate the rows
            print("----------")


def winning_criterion(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 4, 8],
        [2, 4, 6],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8]
    ]
    for groups in winning_combinations:
        if board[groups[0]] == board[groups[1]] == board[groups[2]] == player:
            return True
    return False


# To check if the game is tie or not
def Full(board):
    return " " not in board  # not in operator checks the value is present or not in the list or sequence


def bot(board, player):
    empty_pos = [i for i in range(9) if board[i] == " "]  # only the places which are empty can be used by the bot
    move = random.choice(empty_pos)
    board[move] = player


def human(board, player):
    while True:
        try:
            move = int(input("Enter your move(1-9): "))
            if board[move-1] == " ":
                board[move-1] = player  # whatever the player has chosen between O or X should be enterd in the empty space
                break  # exit  the loop after a valid move
            else:
                print("The Position is already occupied!!")

        except (ValueError, IndexError):
            print("Invalid input!Enter something between 0 to 8")


def play():
    # DIFFERENT METHOD TO INITIALIZE BOARD
    # board = [] #initialize board
    # for index in range(9):
    # board.append(" ")  #better way is to write like this board = [" "for _ in range(9)] it is a concise way _ is used as we don't want numbers to be printed we just want to repeat the step 9 times
    # board = [" " for i in range(9)]  # Using 'i' instead of '_'
    # also like board =[""]*9 initialize 9 elements before only and then
    # for index in range (9):
    # board[index]=" "
    # The one which is using O would play the first chance
    print("Let's Play Tic Tac Toe :)")
    print("The rules are simple If you select O then you'll get the first chance and on selecting X you'll get second chance!!")
    board = [" " for _ in range(9)]
    user_symbol = input("Enter your Preference O or X: ").upper()
    if user_symbol not in ["O", "X"]:
        print("Invalid choice! Defaulting to 'O'.")
        user_symbol = "O"
    bot_symbol = "X" if user_symbol == "O" else "O"
    players = [user_symbol, bot_symbol]

    turn = 0 if user_symbol == "O" else 1
    while True:
        print_board(board)
        if turn % 2 == 0:
            human(board, players[0])
        else:
            print("Computer's turn:")
            bot(board, players[1])
        if winning_criterion(board, players[turn % 2]):
            print_board(board)
            if turn % 2 == 0:
                print("User Wins :) Congo!!!")
            else:
                print("Bot Wins :( ")
            break
        if Full(board):
            print_board(board)
            print("It is a tie")
            break
        turn += 1


if __name__ == "__main__":
    play()