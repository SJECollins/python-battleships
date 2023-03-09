"""
Simple battleship game - just print a board, spawn ships, take user input, check hits
"""

from random import randint

ROWS = 10
COLS = 10

BOARD = [[" "] * 10 for x in range(10)]
ships = []


# First let's try printing a 10 x 10 board
def print_board(board):
    print("    A B C D E F G H I J")
    ends = "   #===================#"
    print(ends)
    num = 1
    for row in board:
        if num != 10:
            print("%d  |%s|" % (num, "|".join(row)))
        else:
            print("%d |%s|" % (num, "|".join(row)))
        num += 1
    print(ends)


# Okay, so what about checking if the ships are overlapping? - not working yet
def check_overlap(coordinates):
    for coords in coordinates:
        if any(coords in ship for ship in ships):
            break
        else:
            ships.append(coordinates)
    
    print(ships)


# # Okay, now create five ships
def create_ships():
    # Get one of the ships
    sizes = [2, 3, 3, 4, 5]

    while len(ships) < 5:
        ship = sizes.pop(0)
    # for ship in sizes:
        start = randint(1, 2)
        if start + ship <= 10:
            direction = randint(0, 1)
            if direction == 0:
                col_letters = []
                row_nums = list(range(start, start + ship))
                col_nums = [randint(1, 10)] * ship
                for col in col_nums:
                    col_letter = chr(col + 97)
                    col_letters.append(col_letter)
                coordinates = list(zip(row_nums, col_letters))
                check_overlap(coordinates)

            else:
                col_letters = []
                col_list = list(range(start, start + ship))
                for col in col_list:
                    col_letter = chr(col + 97)
                    col_letters.append(col_letter)
                row = [randint(1, 10)] * ship
                coordinates = list(zip(row, col_letters))
                check_overlap(coordinates)


# Check for a hit - should it also update the board???
def check_hit(guess):
    hit = False
    for ship in ships:
        if guess in ship:
            hit = True
            if len(ship) == 1:
                ships.remove(ship)
                print("You sunk a battleship!")
                print(f"{len(ships)} ships left")
            else:
                ship.remove(guess)
    
    row = guess[0] - 1
    col_letter = guess[1]
    col = ord(col_letter) - 97

    print("Your guess: ", guess)
    if hit:
        BOARD[row][col] = "X"
        print_board(BOARD)
        print("Your guess: ", guess)
        print("Hit! ")
    else:
        BOARD[row][col] = "O"
        print_board(BOARD)
        print("Your guess: ", guess)
        print("Miss!")
    print(ships)


def get_input():
    while True:
        row = int(input("Enter row: "))
        guess = ()
        if row not in range(1, 11):
            print("Please enter a valid row.")
        else:
            guess = guess + (row, )
            break
    while True:
        col = input("Enter column: ").lower()
        if col not in "abcdefghij":
            print("Please enter a valid column: ")
        else:
            guess = guess + (col, )
            break
    check_hit(guess)


def startGame():
    print("Welcome to Battleships!")
    print("When prompted, enter the row number, then column letter you wish to attack.")
    print("Destroy all 5 of the computer's ships to win!")
    print_board(BOARD)
    create_ships()


def endGame():
    print("You sunk all the battleships!")
    play_again = input("Play again? yes/no: ").lower()
    if play_again == "yes":
        startGame()
    else:
        print("SEE YA!")


if __name__ == "__main__":
    startGame()

    while len(ships) > 0:
        get_input()

    endGame()
