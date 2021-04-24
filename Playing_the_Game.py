import Board as board
import Board_Setup as bs


def turns():
    while 'C' or 'B' or 'D' or 'R' or 'S' in board.board_cpu():
        shot = input("Please select a coordinate to shoot at.\n")
        while shot not in board.board_user.keys() or board.board_cpu[shot] == "O" or board.board_cpu[shot] == "X":
            shot = input("Please select a coordinate that you have not shot at yet\n")
        if board.board_cpu[shot] != " ":
            board.board_cpu[shot] = 'X'
            print("You hit a ship!")
        else:
            board.board_cpu[shot] = 'O'
            print("That was a miss!")
        board.print_board_cpu()
    return print("You have destroyed all ships!")
