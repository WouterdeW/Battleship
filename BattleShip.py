import Board as board

# Carrier (c) - 5
# Battleship (b) - 4
# Cruiser (r) - 3
# Submarine (s) - 3
# Destroyer (d) - 2

ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
lengths = [5, 4, 3, 3, 2]


def orientation_ship(ship_letter, length, ship_start):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)
    orientation = str(input(
        "Would you like to like the bow to point? North (N), East (E), South (S) or West (W)?\n Please pick a letter: ")).lower()
    while orientation not in ["n", "e", "s", "w"]:
        orientation = str(input("Please select N/E/S/W: ")).lower()

    while not is_on_board(ship_start, length, orientation) or is_overlapping(ship_start, length, orientation):
        orientation = str(input(
            "Sorry, this is not possible, the ship would be out of bounds or overlapping another ship.\n Please select N/E/S/W: ")).lower()
        while orientation not in ["n", "e", "s", "w"]:
            orientation = str(input("Please select N/E/S/W: ")).lower()

    if orientation == 'n':
        for i in range(length):
            coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1]
            board.board[coordinate] = ship_letter
    elif orientation == 's':
        for i in range(length):
            coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1]
            board.board[coordinate] = ship_letter
    elif orientation == "e":
        for i in range(length):
            coordinate = ship_start[0] + str(int(ship_start[1]) + i)
            board.board[coordinate] = ship_letter
    elif orientation == 'w':
        for i in range(length):
            coordinate = ship_start[0] + str(int(ship_start[1]) - i)
            board.board[coordinate] = ship_letter


def is_on_board(ship_start, length, orientation):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)
    coordinate_numbers = [i for i in range(1, 11)]
    ship_start_number = int(ship_start[1])
    ship_start_number_idx = coordinate_numbers.index(ship_start_number)
    if orientation == 'n':
        if ship_start_letter_idx - (length - 1) < 0:
            return False
        # try:
        #    board.rows[ship_start_letter_idx - (length - 1)]
        # except IndexError:
        #    return False
        return True
    elif orientation == 's':
        if ship_start_letter_idx + (length - 1) > 9:
            return False
        # try:
        #    board.rows[ship_start_letter_idx + (length - 1)]
        # except IndexError:
        #    return False
        return True
    elif orientation == "e":
        if ship_start_number_idx + (length - 1) > 9:
            return False
        # try:
        #    coordinate_numbers[ship_start_number_idx + (length - 1)]
        # except IndexError:
        #    return False
        return True
    elif orientation == "w":
        if ship_start_number_idx - (length - 1) < 0:
            return False
        # try:
        #    coordinate_numbers[ship_start_number_idx - (length - 1)]
        # except IndexError:
        #    return False
        return True


def is_overlapping(ship_start, length, orientation=None):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)
    if orientation == 'n':
        for i in range(length):
            coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1]
            if board.board[coordinate] != " ":
                return True
            return False
    elif orientation == 's':
        for i in range(length):
            coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1]
            if board.board[coordinate] != " ":
                return False
            return True
    elif orientation == "e":
        for i in range(length):
            coordinate = ship_start[0] + str(int(ship_start[1]) + i)
            if board.board[coordinate] != " ":
                return False
            return True
    elif orientation == 'w':
        for i in range(length):
            coordinate = ship_start[0] + str(int(ship_start[1]) - i)
            if board.board[coordinate] != " ":
                return False
            return True
    else:
        if board.board[ship_start] == " ":
            return False
        return True


def place_ship(shipname, length):
    question = "Where would you like to place the stern of the {one}? Please select one of the coordinates\n".format(
        one=shipname)
    ship_start = str(input(question)).lower()
    while ship_start not in board.board.keys() or is_overlapping(ship_start, 1):
        ship_start = input(
            "This is not a valid coordinate or this coordinate is already taken. Please select another one\n")
    orientation_ship(shipname[0], length, ship_start)


def board_setup():
    board.print_board()
    for i in range(5):
        place_ship(ships[i], lengths[i])
        board.print_board()


board_setup()
