import Board as board
import Board_Setup as bs

lines = "--------------------------------------------------------"


def turns(player, hits_user=0, hits_cpu=0):
    # even = user, uneven = cpu
    if player % 2 == 0:
        print(lines)
        print("IT IS YOUR TURN!")
        board.print_board_cpu_display()
        shot = input("Please select a coordinate to shoot at.\n")
        while shot not in board.board_user.keys() or board.board_cpu[shot] == "O" or board.board_cpu[shot] == "X":
            shot = input("Please select a coordinate that you have not shot at yet\n")

        if board.board_cpu[shot] != " ":
            board.board_cpu[shot] = 'X'
            board.board_cpu_display[shot] = 'X'
            board.print_board_cpu_display()
            print("You hit a ship!")
            hits_user += 1
        else:
            board.board_cpu[shot] = 'O'
            board.board_cpu_display[shot] = 'O'
            board.print_board_cpu_display()
            print("That was a miss!")

        if hits_user == 17:
            print("You have destroyed all your opponent's ships!")
            return
        else:
            return turns(player + 1, hits_user, hits_cpu)
    elif player % 2 != 0:
        print(lines)
        print("IT IS YOUR OPPONENT'S TURN!")
        shot = bs.random_coordinate()
        while board.board_user[shot] == "O" or board.board_user[shot] == "X":
            shot = bs.random_coordinate()

        if board.board_user[shot] != " ":
            board.board_user[shot] = 'X'
            board.print_board_user()
            print("The CPU hit one of your ships!")
            hits_cpu += 1
        else:
            board.board_user[shot] = 'O'
            board.print_board_user()
            print("That was a miss!")

        if hits_cpu == 17:
            print("Your opponent has destroyed all your ships!")
            return
        else:
            return turns(player + 1, hits_user, hits_cpu)


def ships_on_board(board):
    board_items = []

    for item in board.items():
        board_items.append(item[1])
    print(board_items)
    if 'C' or 'B' or 'D' or 'R' or 'S' not in board_items:
        return False
    else:
        return True
