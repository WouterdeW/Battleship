import string

board = {}
rows = string.ascii_lowercase[:10]

for letter in rows:
    for i in range(1, 11):
        board[letter+str(i)] = " "

hor_vert = "___|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____"
vert = "   |     |     |     |     |     |     |     |     |     |     "


def print_board():
    print("   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  ")
    print(hor_vert)
    print(vert)
    print(" A |  "+board["a1"]+"  |  "+board["a2"]+"  |  "+board["a3"]+"  |  "+board["a4"]+"  |  "+board["a5"]+"  |  " +
          board["a6"]+"  |  "+board["a7"]+"  |  "+board["a8"]+"  |  "+board["a9"]+"  | "+board["a10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" B |  "+board["b1"]+"  |  "+board["b2"]+"  |  "+board["b3"]+"  |  "+board["b4"]+"  |  "+board["b5"]+"  |  " +
          board["b6"]+"  |  "+board["b7"]+"  |  "+board["b8"]+"  |  "+board["b9"]+"  |  "+board["b10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" C |  "+board["c1"]+"  |  "+board["c2"]+"  |  "+board["c3"]+"  |  "+board["c4"]+"  |  "+board["c5"]+"  |  " +
          board["c6"]+"  |  "+board["c7"]+"  |  "+board["c8"]+"  |  "+board["c9"]+"  |  "+board["c10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" D |  "+board["d1"]+"  |  "+board["d2"]+"  |  "+board["d3"]+"  |  "+board["d4"]+"  |  "+board["d5"] +
          "  |  " + board["d6"]+"  |  "+board["d7"]+"  |  "+board["d8"]+"  |  "+board["d9"]+"  |  "+board["d10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" E |  "+board["e1"]+"  |  "+board["e2"]+"  |  "+board["e3"]+"  |  "+board["e4"]+"  |  "+board["e5"] +
          "  |  " + board["e6"]+"  |  "+board["e7"]+"  |  "+board["e8"]+"  |  "+board["e9"]+"  |  "+board["e10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" F |  "+board["f1"]+"  |  "+board["f2"]+"  |  "+board["f3"]+"  |  "+board["f4"]+"  |  "+board["f5"] +
          "  |  "+board["f6"]+"  |  "+board["f7"]+"  |  "+board["f8"]+"  |  "+board["f9"]+"  |  "+board["f10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" G |  "+board["g1"]+"  |  "+board["g2"]+"  |  "+board["g3"]+"  |  "+board["g4"]+"  |  "+board["g5"] +
          "  |  " + board["g6"]+"  |  "+board["g7"]+"  |  "+board["g8"]+"  |  "+board["g9"]+"  |  "+board["g10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" H |  "+board["h1"]+"  |  "+board["h2"]+"  |  "+board["h3"]+"  |  "+board["h4"]+"  |  "+board["h5"] +
          "  |  " + board["h6"]+"  |  "+board["h7"]+"  |  "+board["h8"]+"  |  "+board["h9"]+"  |  "+board["h10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" I |  "+board["i1"]+"  |  "+board["i2"]+"  |  "+board["i3"]+"  |  "+board["i4"]+"  |  "+board["i5"] +
          "  |  " + board["i6"]+"  |  "+board["i7"]+"  |  "+board["i8"]+"  |  "+board["i9"]+"  |  "+board["i10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" J |  "+board["j1"]+"  |  "+board["j2"]+"  |  "+board["j3"]+"  |  "+board["j4"]+"  |  "+board["j5"] +
          "  |  " + board["j6"]+"  |  "+board["j7"]+"  |  "+board["j8"]+"  |  "+board["j9"]+"  |  "+board["j10"]+"  ")
    print(hor_vert)
