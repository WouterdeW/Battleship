import Board_Setup as bs
import Playing_the_Game as play

print("""
WELCOME TO BATTLESHIP!!

You will be playing against our computer.
First, you will set-up your board.
""")
input("Press any key to continue")
bs.board_setup()
print("""
Above is how your board will look.
On your turn, call out a letter and a number that identifies a row and column on your target grid.
If you 'MISS', this will be marked with an 'O' on your opponent's board.
If you 'HIT', this will be marked with an 'X' on your opponent's board.
The computer and you will take turns trying to destroy all of each other's ships.
The first to destroy all the ships wins.
""")
input("Press any key to get started!")
play.turns(0)
