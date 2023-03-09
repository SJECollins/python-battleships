"""
Versus the computer
"""
from random import randint

COMP_BOARD = [[" "] * 10 for x in range(10)]
USER_BOARD = [[" "] * 10 for y in range(10)]

COMP_SHIPS = []
USER_SHIPS = []


def print_player(board):
    print("          PLAYER", end = "")
    yield
    print("      A B C D E F G H I J", end = "")
    yield
    ends = "    #===================#"
    print(ends, end = "")
    yield
    num = 1
    for row in board:
        if num != 10:
            print("%d   |%s|" % (num, "|".join(row)), end = "")
            yield
        else:
            print("%d  |%s|" % (num, "|".join(row)), end = "")
            yield
        num += 1
    print(ends, end = "")
    yield


def print_comp(board):
    print("      COMPUTER       ", end = "")
    yield
    print(" A B C D E F G H I J", end = "")
    yield
    ends = "#===================#"
    print(ends, end = "")
    yield
    num = 1
    for row in board:
        if num != 10:
            print("|%s|" % ("|".join(row)), end = "")
            yield
        else:
            print("|%s|" % ("|".join(row)), end = "")
            yield
        num += 1
    print(ends, end = "")
    yield


def print_boards():
    board_one, board_two = print_comp(COMP_BOARD), print_player(USER_BOARD)

    while True:
        try:
            next(board_one)
            print("   ", end = "")
            next(board_two)
            print()
        except StopIteration:
            break


def check_overlap(coordinates, ship, ships, visible):
    taken = False
    for coords in coordinates:
        if any(coords in ship_list for ship_list in ships):
            taken = True
            break
    
    if taken:
        return create_ships(ship, ships, visible)
    else:
        if visible:
            USER_SHIPS.append(coordinates)
            for coords in coordinates:
                row = coords[0] - 1
                col_letter = coords[1]
                col = ord(col_letter) - 97
                USER_BOARD[row][col] = "$"
                print("Should print for every coordinate")
        else:
            COMP_SHIPS.append(coordinates)


def create_ships(ship, ships, visible):
    start = randint(1, 10 - ship)
    direction = randint(0, 1)
    if direction == 0:
        col_letters = []
        row_nums = list(range(start, start + ship))
        col_nums = [randint(1, 10)] * ship
        for col in col_nums:
            col_letter = chr(col + 96)
            col_letters.append(col_letter)
        coordinates = list(zip(row_nums, col_letters))
        check_overlap(coordinates, ship, ships, visible)
    else:
        col_letters = []
        col_list = list(range(start, start + ship))
        for col in col_list:
            col_letter = chr(col + 96)
            col_letters.append(col_letter)
        row = [randint(1, 10)] * ship
        coordinates = list(zip(row, col_letters))
        check_overlap(coordinates, ship, ships, visible)


def check_hit(guess, ships, board, player):
    hit = False
    for ship in ships:
        if guess in ship:
            hit = True
            if len(ship) == 1:
                ships.remove(ship)
                if player:
                    print("You sunk a battleship!")
                else:
                    print("You lost a battleship!")
            else:
                ship.remove(guess)
    
    row = guess[0] - 1
    col_letter = guess[1]
    col = ord(col_letter) - 97

    if player:
        print("Your guess: ", guess)
    else:
        print("Enemy move: ", guess)
    if hit:
        board[row][col] = "X"
        print("Hit! ")
    else:
        board[row][col] = "O"
        print("Miss!")


def get_user_input():
    guess = ()
    print(f"The enemy has {len(COMP_SHIPS)} battleships remaining.")
    print(f"You have {len(USER_SHIPS)} battleships remaining.")
    print("Enter the coordinates for your missile below!")
    while True:
        row_num = input("Enter row: ").strip()
        if row_num is "" or row_num not in "12345678910":
            print("Please enter a valid row.")
        else:
            row = int(row_num)
            guess = guess + (row, )
            break
    while True:
        col = input("Enter column: ").strip().lower()
        if col not in "abcdefghij":
            print("Please enter a valid column: ")
        else:
            guess = guess + (col, )
            break
    player = True
    check_hit(guess, COMP_SHIPS, COMP_BOARD, player)


def get_comp_move():
    move = ()
    row = randint(1, 10)
    move = move + (row, )
    col_num = randint(1, 10)
    col = chr(col_num + 96)
    move = move + (col, )
    player = False
    check_hit(move, USER_SHIPS, USER_BOARD, player)


def start_game():
    user_sizes = [2, 3, 3, 4, 5]
    comp_sizes = [2, 3, 3, 4, 5]
    print("Welcome to Battleships!")
    print("When prompted, enter the row number, then column letter you wish to attack.")
    print("Destroy all 5 of the computer's ships to win!")

    while len(USER_SHIPS) < 5:
        ship = user_sizes.pop(0)
        visible = True
        create_ships(ship, USER_SHIPS, visible)
    
    while len(COMP_SHIPS) < 5:
        ship = comp_sizes.pop(0)
        visible = False
        create_ships(ship, COMP_SHIPS, visible)
    
    print_boards()


def end_game():
    if len(USER_SHIPS) < len(COMP_SHIPS):
        print("You lose!")
    else:
        print("You sunk all their battleships!")


def main():
    start_game()

    while len(USER_SHIPS) > 0 and len(COMP_SHIPS) > 0:
        get_user_input()
        get_comp_move()
        print_boards()

    end_game()

main()