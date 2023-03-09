"""
Simple battleship game - just print a board, spawn ships, take user input, check hits
"""

from random import randint

ROWS = 10
COLS = 10

BOARD = [[" "] * 10 for x in range(10)]

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

print_board(BOARD)

# # Okay, now print ships to board - randomly? Print 5 of them? Everyons seems to use the same
ships = []

def add_ships():
    # Get one of the ships
    sizes = [1, 3, 3, 4, 5]

    for ship in sizes:
        start = randint(0, 1)
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
                print(coordinates)
                ships.append(coordinates)

            else:
                col_letters = []
                col_list = list(range(start, start + ship))
                for col in col_list:
                    col_letter = chr(col + 97)
                    col_letters.append(col_letter)
                row = [randint(1, 10)] * ship
                coordinates = list(zip(row, col_letters))
                print(coordinates)
                ships.append(coordinates)
    
    print(ships)
    print(len(ships))
# Need to check for overlap!

add_ships()

# Check for a hit - should it also update the board???
def check_hit(guess):
    print("called")
    print(ships)
    hit = False
    for ship in ships:
        if guess in ship:
            hit = True
            print(ship)
            if len(ship) == 1:
                ships.remove(ship)
                print("you sunk my battleship!")
                print(f"{len(ships)} left")
            else:
                ship.remove(guess)
                print(ship)
    
    if hit:
        print("hit")
    else:
        print("miss")

    print(ships)


def get_input():
    row = int(input("Enter row: "))
    print(row)
    print(list(range(1, 11)))
    guess = ()
    if row not in range(1, 11):
        print("Please enter a valid row.")
    else:
        guess = guess + (row, )
        col = input("Enter column: ").lower()
        if col not in "abcdefghij":
            print("Please enter a valid column: ")
        else:
            guess = guess + (col, )
    print(col, row)
    print(guess)
    # return guess
    check_hit(guess)


get_input()


# Okay, so what about checking if the ships are overlapping?

def check_overlap():
    

