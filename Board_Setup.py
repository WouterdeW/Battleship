import Board as board
import random
# Carrier (c) - 5
# Battleship (b) - 4
# Cruiser (r) - 3
# Submarine (s) - 3
# Destroyer (d) - 2

ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
lengths = [5, 4, 3, 3, 2]


def random_coordinate():
    random_coordinate = random.choice(board.rows) + str(random.randrange(1, 11))
    return random_coordinate


def random_direction():
    return random.choice(["n", "e", "s", "w"])


def direction_ship(ship_letter, length, ship_start, cpu=None):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)

    if cpu:
        direction = random_direction()
        while (not is_on_board(ship_start, length, direction)) or (is_overlapping(ship_start, length, direction, True)):
            direction = random_direction()

    else:
        direction = str(input(
            "Would you like to like the bow to point? North (N), East (E), South (S) or West (W)?\n Please pick a letter: ")).lower()
        while direction not in ["n", "e", "s", "w"]:
            direction = str(input("Please select N/E/S/W: ")).lower()

        while (not is_on_board(ship_start, length, direction)) or (is_overlapping(ship_start, length, direction)):
            direction = str(input(
                "Sorry, this is not possible, the ship would be out of bounds or overlapping another ship.\n Please select N/E/S/W: ")).lower()
            while direction not in ["n", "e", "s", "w"]:
                direction = str(input("Please select N/E/S/W: ")).lower()

    if cpu:
        if direction == 'n':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1:]
                board.board_cpu[coordinate] = ship_letter
        elif direction == 's':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1:]
                board.board_cpu[coordinate] = ship_letter
        elif direction == "e":
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1:]) + i)
                board.board_cpu[coordinate] = ship_letter
        elif direction == 'w':
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1:]) - i)
                board.board_cpu[coordinate] = ship_letter
    else:
        if direction == 'n':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1:]
                board.board_user[coordinate] = ship_letter
        elif direction == 's':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1:]
                board.board_user[coordinate] = ship_letter
        elif direction == "e":
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1:]) + i)
                board.board_user[coordinate] = ship_letter
        elif direction == 'w':
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1:]) - i)
                board.board_user[coordinate] = ship_letter


def is_on_board(ship_start, length, direction):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)
    coordinate_numbers = [i for i in range(1, 11)]
    ship_start_number = int(ship_start[1])
    ship_start_number_idx = coordinate_numbers.index(ship_start_number)
    if direction == 'n':
        if ship_start_letter_idx - (length - 1) < 0:
            return False
        return True
    elif direction == 's':
        if ship_start_letter_idx + (length - 1) > 9:
            return False
        return True
    elif direction == "e":
        if ship_start_number_idx + (length - 1) > 9:
            return False
        return True
    elif direction == "w":
        if ship_start_number_idx - (length - 1) < 0:
            return False
        return True


def is_overlapping(ship_start, length, direction=None, cpu=None):
    ship_start_letter = ship_start[0]
    ship_start_letter_idx = board.rows.index(ship_start_letter)

    if cpu:
        if direction == 'n':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1]
                if board.board_cpu[coordinate] != " ":
                    return True
            return False
        elif direction == 's':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1]
                if board.board_cpu[coordinate] != " ":
                    return True
            return False
        elif direction == "e":
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1]) + i)
                if board.board_cpu[coordinate] != " ":
                    return True
            return False
        elif direction == 'w':
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1]) - i)
                if board.board_cpu[coordinate] != " ":
                    return True
            return False
        else:
            if board.board_cpu[ship_start] == " ":
                return False
            return True
    else:
        if direction == 'n':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx - i] + ship_start[1]
                if board.board_user[coordinate] != " ":
                    return True
            return False
        elif direction == 's':
            for i in range(length):
                coordinate = board.rows[ship_start_letter_idx + i] + ship_start[1]
                if board.board_user[coordinate] != " ":
                    return True
            return False
        elif direction == "e":
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1]) + i)
                if board.board_user[coordinate] != " ":
                    return True
            return False
        elif direction == 'w':
            for i in range(length):
                coordinate = ship_start[0] + str(int(ship_start[1]) - i)
                if board.board_user[coordinate] != " ":
                    return True
            return False
        else:
            if board.board_user[ship_start] == " ":
                return False
            return True


def place_ship(shipname, length, cpu=None):
    if not cpu:
        question = "Where would you like to place the stern of the {one}? Please select one of the coordinates\n".format(
            one=shipname)
        ship_start = str(input(question)).lower()
        while ship_start not in board.board_user.keys() or is_overlapping(ship_start, 1):
            ship_start = input(
                "This is not a valid coordinate or this coordinate is already taken. Please select another one\n")
        direction_ship(shipname[0], length, ship_start)
    else:
        ship_start = random_coordinate()
        while is_overlapping(ship_start, 1, None, True):
            ship_start = random_coordinate()
        direction_ship(shipname[0], length, ship_start, True)


def board_setup():
    board.print_board_user()
    for i in range(5):
        place_ship(ships[i], lengths[i])
        board.print_board_user()

    for i in range(5):
        place_ship(ships[i], lengths[i], True)
