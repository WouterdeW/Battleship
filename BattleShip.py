import Board as board

# Carrier (c) - 5
# Battleship (b) - 4
# Cruiser (r) - 3
# Submarine (s) - 3
# Destroyer (d) - 2


def orientation_ship(shipname, length, ship_start):
    ship_start_letter = ship_start[0]
    ship_start_idx = board.rows.find(ship_start_letter)
    orientation = str(input(
        "Would you like to like the bow to point? North (N), East (E), South (S) or West (W)?\n Please pick a letter: ")).lower()
    while orientation not in ["n", "e", "s", "w"]:
        orientation = str(input("Please select N/E/S/W: ")).lower()

    while not is_possible(ship_start, length, orientation):
        orientation = str(input(
            "Sorry, this is not possible, the ship would be out of bounds.\n Please select N/E/S/W: ")).lower()
        while orientation not in ["n", "e", "s", "w"]:
            orientation = str(input("Please select N/E/S/W: ")).lower()

    if orientation == 'n':
        for i in range(length):
            coordinate = board.rows[ship_start_idx - i] + ship_start[1]
            board.board[coordinate] = shipname
    elif orientation == 's':
        for i in range(length):
            coordinate = board.rows[ship_start_idx + i] + ship_start[1]
            board.board[coordinate] = shipname
    elif orientation == "e":
        for i in range(length):
            coordinate = ship_start[0] + str(int(ship_start[1]) + i)
            board.board[coordinate] = shipname
    elif orientation == 'w':
        coordinate = ship_start[0] + str(int(ship_start[1]) - i)
        board.board[coordinate] = shipname


def is_possible(ship_start, length, orientation):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.find(ship_start_letter)
    coordinate_numbers = [i for i in range(1, 11)]
    ship_start_number = int(ship_start[1])
    ship_start_number_idx = coordinate_numbers.find(ship_start_number)
    if orientation == 'n':
        try:
            board.rows[ship_start_letter_idx - (length - 1)]
        except IndexError:
            return False
        return True
    elif orientation == 's':
        try:
            board.rows[ship_start_letter_idx + (length - 1)]
        except IndexError:
            return False
        return True
    elif orientation == "e":
        try:
            coordinate_numbers[ship_start_number_idx + (length - 1)]
        except IndexError:
            return False
        return True
    elif orientation == "w":
        try:
            coordinate_numbers[ship_start_number_idx - (length - 1)]
        except IndexError:
            return False
        return True


def place_ship(shipname, length):
    ship_start = input(
        "Where would you like to place the stern of the {0}? Please select one of the coordinates\n").format(shipname)
    while str(ship_start) not in board.board.keys():
        ship_start = input("Dude.. do you know how coordinates work? Just pick a valid one.\n")
    orientation_ship(shipname, length, ship_start)


orientation_ship('c', 2, "b2")
board.print_board()
