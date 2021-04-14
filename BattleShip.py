import Board as board


if "a1" in board.board.keys():
    print("hello")


def place_carrier():
    carrier_start = input(
        "Where would you like to place the stern of the Carrier? Please select one of the coordinates\n")
    while carier_start not in board.board.keys():
        input("Dude.. do you know how coordinates work? Just pick a valid one.\n")
