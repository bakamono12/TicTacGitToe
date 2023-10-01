from colorama import init
from termcolor import colored
import replit

init()

success = {
    "1": [(1, 5, 9), (1, 4, 7), (1, 2, 3)],
    "2": [(1, 2, 3), (2, 5, 8)],
    "3": [(1, 2, 3), (3, 6, 9), (3, 5, 7)],
    "4": [(1, 4, 7), (4, 5, 6)],
    "5": [(1, 5, 9), (2, 5, 8), (3, 5, 7), (4, 5, 6)],
    "6": [(3, 6, 9), (4, 5, 6)],
    "7": [(1, 4, 7), (3, 5, 7), (7, 8, 9)],
    "8": [(2, 5, 8), (7, 8, 9)],
    "9": [(1, 5, 9), (3, 6, 9), (7, 8, 9)]
}

replit.clear()
print("\n")
print(colored("Welcome to Tic Tac Toe", "green"))
print(colored("Player 1 is X", "red"))
print(colored("Player 2 is O", "blue"),"\n")
continue_game = input("Do you want to play? (Y/N): ")
if continue_game.lower() == "y":
    print("Position pattern for playing the game")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
else:
    exit()


# Define a function to print the Tic Tac Toe board
def print_board(board):
    for row in range(1, 10, 3):
        print(f" {board[row]} | {board[row + 1]} | {board[row + 2]} ")
        if row < 7:
            print("------------")


# Create an empty board
board = {i: ' ' for i in range(1, 10)}


def check_win(player):
    """Check for the winning combination"""
    for i in success:
        for j in success[i]:
            if j[0] in player and j[1] in player and j[2] in player:
                return True
    return False


game_on = True
player1 = []
player2 = []

while game_on:
    p1 = check_win(player1)
    p2 = check_win(player2)
    if p1:
        game_on = False
        print("\n")
        print(colored("Player 1 wins", "red"))
        print("\n")
    elif p2:
        game_on = False
        print("\n", colored("Player 2 wins", "blue"), "\n")
    else:
        if len(player1) + len(player2) == 9:
            game_on = False
            print("\n", colored("Draw", "green"), "\n")
        else:
            try:
                if len(player1) == len(player2):
                    move = int(input("\nPlayer 1, enter a number: "))
                    if move in player1:
                        print("\nInvalid move, position occupied aka you already played there.\n")
                    elif move not in player2:
                        player1.append(move)
                        print("\n")
                        board[move] = '\033[31mX\033[00m'
                    else:
                        print("\nInvalid move, position occupied aka player 2 already played there.\n")
                else:
                    move = int(input("\nPlayer 2, enter a number: "))
                    if move in player2:
                        print("\nInvalid move, position occupied aka you  already played there.\n")
                    elif move not in player1:
                        player2.append(move)
                        print("\n")
                        board[move] = '\033[34mO\033[00m'
                    else:
                        print("\nInvalid move, position occupied aka player 1 already played there.\n")
            except ValueError:
                print("\nInvalid move, enter a number.\n")
    print_board(board)
