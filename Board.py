import string

board_user = {}
board_cpu = {}
board_cpu_display = {}
rows = string.ascii_lowercase[:10]

for letter in rows:
    for i in range(1, 11):
        board_user[letter+str(i)] = " "
        board_cpu[letter+str(i)] = " "
        board_cpu_display[letter+str(i)] = " "

hor_vert = "___|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____"
vert = "   |     |     |     |     |     |     |     |     |     |     "


def print_board_user():
    print("   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  ")
    print(hor_vert)
    print(vert)
    print(" A |  "+board_user["a1"]+"  |  "+board_user["a2"]+"  |  "+board_user["a3"]+"  |  "+board_user["a4"]+"  |  "+board_user["a5"]+"  |  " +
          board_user["a6"]+"  |  "+board_user["a7"]+"  |  "+board_user["a8"]+"  |  "+board_user["a9"]+"  |  "+board_user["a10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" B |  "+board_user["b1"]+"  |  "+board_user["b2"]+"  |  "+board_user["b3"]+"  |  "+board_user["b4"]+"  |  "+board_user["b5"]+"  |  " +
          board_user["b6"]+"  |  "+board_user["b7"]+"  |  "+board_user["b8"]+"  |  "+board_user["b9"]+"  |  "+board_user["b10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" C |  "+board_user["c1"]+"  |  "+board_user["c2"]+"  |  "+board_user["c3"]+"  |  "+board_user["c4"]+"  |  "+board_user["c5"]+"  |  " +
          board_user["c6"]+"  |  "+board_user["c7"]+"  |  "+board_user["c8"]+"  |  "+board_user["c9"]+"  |  "+board_user["c10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" D |  "+board_user["d1"]+"  |  "+board_user["d2"]+"  |  "+board_user["d3"]+"  |  "+board_user["d4"]+"  |  "+board_user["d5"] +
          "  |  " + board_user["d6"]+"  |  "+board_user["d7"]+"  |  "+board_user["d8"]+"  |  "+board_user["d9"]+"  |  "+board_user["d10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" E |  "+board_user["e1"]+"  |  "+board_user["e2"]+"  |  "+board_user["e3"]+"  |  "+board_user["e4"]+"  |  "+board_user["e5"] +
          "  |  " + board_user["e6"]+"  |  "+board_user["e7"]+"  |  "+board_user["e8"]+"  |  "+board_user["e9"]+"  |  "+board_user["e10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" F |  "+board_user["f1"]+"  |  "+board_user["f2"]+"  |  "+board_user["f3"]+"  |  "+board_user["f4"]+"  |  "+board_user["f5"] +
          "  |  "+board_user["f6"]+"  |  "+board_user["f7"]+"  |  "+board_user["f8"]+"  |  "+board_user["f9"]+"  |  "+board_user["f10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" G |  "+board_user["g1"]+"  |  "+board_user["g2"]+"  |  "+board_user["g3"]+"  |  "+board_user["g4"]+"  |  "+board_user["g5"] +
          "  |  " + board_user["g6"]+"  |  "+board_user["g7"]+"  |  "+board_user["g8"]+"  |  "+board_user["g9"]+"  |  "+board_user["g10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" H |  "+board_user["h1"]+"  |  "+board_user["h2"]+"  |  "+board_user["h3"]+"  |  "+board_user["h4"]+"  |  "+board_user["h5"] +
          "  |  " + board_user["h6"]+"  |  "+board_user["h7"]+"  |  "+board_user["h8"]+"  |  "+board_user["h9"]+"  |  "+board_user["h10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" I |  "+board_user["i1"]+"  |  "+board_user["i2"]+"  |  "+board_user["i3"]+"  |  "+board_user["i4"]+"  |  "+board_user["i5"] +
          "  |  " + board_user["i6"]+"  |  "+board_user["i7"]+"  |  "+board_user["i8"]+"  |  "+board_user["i9"]+"  |  "+board_user["i10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" J |  "+board_user["j1"]+"  |  "+board_user["j2"]+"  |  "+board_user["j3"]+"  |  "+board_user["j4"]+"  |  "+board_user["j5"] +
          "  |  " + board_user["j6"]+"  |  "+board_user["j7"]+"  |  "+board_user["j8"]+"  |  "+board_user["j9"]+"  |  "+board_user["j10"]+"  ")
    print(hor_vert)


def print_board_cpu():
    print("   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  ")
    print(hor_vert)
    print(vert)
    print(" A |  "+board_cpu["a1"]+"  |  "+board_cpu["a2"]+"  |  "+board_cpu["a3"]+"  |  "+board_cpu["a4"]+"  |  "+board_cpu["a5"]+"  |  " +
          board_cpu["a6"]+"  |  "+board_cpu["a7"]+"  |  "+board_cpu["a8"]+"  |  "+board_cpu["a9"]+"  |  "+board_cpu["a10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" B |  "+board_cpu["b1"]+"  |  "+board_cpu["b2"]+"  |  "+board_cpu["b3"]+"  |  "+board_cpu["b4"]+"  |  "+board_cpu["b5"]+"  |  " +
          board_cpu["b6"]+"  |  "+board_cpu["b7"]+"  |  "+board_cpu["b8"]+"  |  "+board_cpu["b9"]+"  |  "+board_cpu["b10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" C |  "+board_cpu["c1"]+"  |  "+board_cpu["c2"]+"  |  "+board_cpu["c3"]+"  |  "+board_cpu["c4"]+"  |  "+board_cpu["c5"]+"  |  " +
          board_cpu["c6"]+"  |  "+board_cpu["c7"]+"  |  "+board_cpu["c8"]+"  |  "+board_cpu["c9"]+"  |  "+board_cpu["c10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" D |  "+board_cpu["d1"]+"  |  "+board_cpu["d2"]+"  |  "+board_cpu["d3"]+"  |  "+board_cpu["d4"]+"  |  "+board_cpu["d5"] +
          "  |  " + board_cpu["d6"]+"  |  "+board_cpu["d7"]+"  |  "+board_cpu["d8"]+"  |  "+board_cpu["d9"]+"  |  "+board_cpu["d10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" E |  "+board_cpu["e1"]+"  |  "+board_cpu["e2"]+"  |  "+board_cpu["e3"]+"  |  "+board_cpu["e4"]+"  |  "+board_cpu["e5"] +
          "  |  " + board_cpu["e6"]+"  |  "+board_cpu["e7"]+"  |  "+board_cpu["e8"]+"  |  "+board_cpu["e9"]+"  |  "+board_cpu["e10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" F |  "+board_cpu["f1"]+"  |  "+board_cpu["f2"]+"  |  "+board_cpu["f3"]+"  |  "+board_cpu["f4"]+"  |  "+board_cpu["f5"] +
          "  |  "+board_cpu["f6"]+"  |  "+board_cpu["f7"]+"  |  "+board_cpu["f8"]+"  |  "+board_cpu["f9"]+"  |  "+board_cpu["f10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" G |  "+board_cpu["g1"]+"  |  "+board_cpu["g2"]+"  |  "+board_cpu["g3"]+"  |  "+board_cpu["g4"]+"  |  "+board_cpu["g5"] +
          "  |  " + board_cpu["g6"]+"  |  "+board_cpu["g7"]+"  |  "+board_cpu["g8"]+"  |  "+board_cpu["g9"]+"  |  "+board_cpu["g10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" H |  "+board_cpu["h1"]+"  |  "+board_cpu["h2"]+"  |  "+board_cpu["h3"]+"  |  "+board_cpu["h4"]+"  |  "+board_cpu["h5"] +
          "  |  " + board_cpu["h6"]+"  |  "+board_cpu["h7"]+"  |  "+board_cpu["h8"]+"  |  "+board_cpu["h9"]+"  |  "+board_cpu["h10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" I |  "+board_cpu["i1"]+"  |  "+board_cpu["i2"]+"  |  "+board_cpu["i3"]+"  |  "+board_cpu["i4"]+"  |  "+board_cpu["i5"] +
          "  |  " + board_cpu["i6"]+"  |  "+board_cpu["i7"]+"  |  "+board_cpu["i8"]+"  |  "+board_cpu["i9"]+"  |  "+board_cpu["i10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" J |  "+board_cpu["j1"]+"  |  "+board_cpu["j2"]+"  |  "+board_cpu["j3"]+"  |  "+board_cpu["j4"]+"  |  "+board_cpu["j5"] +
          "  |  " + board_cpu["j6"]+"  |  "+board_cpu["j7"]+"  |  "+board_cpu["j8"]+"  |  "+board_cpu["j9"]+"  |  "+board_cpu["j10"]+"  ")
    print(hor_vert)


def print_board_cpu_display():
    print("   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  ")
    print(hor_vert)
    print(vert)
    print(" A |  "+board_cpu_display["a1"]+"  |  "+board_cpu_display["a2"]+"  |  "+board_cpu_display["a3"]+"  |  "+board_cpu_display["a4"]+"  |  "+board_cpu_display["a5"]+"  |  " +
          board_cpu_display["a6"]+"  |  "+board_cpu_display["a7"]+"  |  "+board_cpu_display["a8"]+"  |  "+board_cpu_display["a9"]+"  |  "+board_cpu_display["a10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" B |  "+board_cpu_display["b1"]+"  |  "+board_cpu_display["b2"]+"  |  "+board_cpu_display["b3"]+"  |  "+board_cpu_display["b4"]+"  |  "+board_cpu_display["b5"]+"  |  " +
          board_cpu_display["b6"]+"  |  "+board_cpu_display["b7"]+"  |  "+board_cpu_display["b8"]+"  |  "+board_cpu_display["b9"]+"  |  "+board_cpu_display["b10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" C |  "+board_cpu_display["c1"]+"  |  "+board_cpu_display["c2"]+"  |  "+board_cpu_display["c3"]+"  |  "+board_cpu_display["c4"]+"  |  "+board_cpu_display["c5"]+"  |  " +
          board_cpu_display["c6"]+"  |  "+board_cpu_display["c7"]+"  |  "+board_cpu_display["c8"]+"  |  "+board_cpu_display["c9"]+"  |  "+board_cpu_display["c10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" D |  "+board_cpu_display["d1"]+"  |  "+board_cpu_display["d2"]+"  |  "+board_cpu_display["d3"]+"  |  "+board_cpu_display["d4"]+"  |  "+board_cpu_display["d5"] +
          "  |  " + board_cpu_display["d6"]+"  |  "+board_cpu_display["d7"]+"  |  "+board_cpu_display["d8"]+"  |  "+board_cpu_display["d9"]+"  |  "+board_cpu_display["d10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" E |  "+board_cpu_display["e1"]+"  |  "+board_cpu_display["e2"]+"  |  "+board_cpu_display["e3"]+"  |  "+board_cpu_display["e4"]+"  |  "+board_cpu_display["e5"] +
          "  |  " + board_cpu_display["e6"]+"  |  "+board_cpu_display["e7"]+"  |  "+board_cpu_display["e8"]+"  |  "+board_cpu_display["e9"]+"  |  "+board_cpu_display["e10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" F |  "+board_cpu_display["f1"]+"  |  "+board_cpu_display["f2"]+"  |  "+board_cpu_display["f3"]+"  |  "+board_cpu_display["f4"]+"  |  "+board_cpu_display["f5"] +
          "  |  "+board_cpu_display["f6"]+"  |  "+board_cpu_display["f7"]+"  |  "+board_cpu_display["f8"]+"  |  "+board_cpu_display["f9"]+"  |  "+board_cpu_display["f10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" G |  "+board_cpu_display["g1"]+"  |  "+board_cpu_display["g2"]+"  |  "+board_cpu_display["g3"]+"  |  "+board_cpu_display["g4"]+"  |  "+board_cpu_display["g5"] +
          "  |  " + board_cpu_display["g6"]+"  |  "+board_cpu_display["g7"]+"  |  "+board_cpu_display["g8"]+"  |  "+board_cpu_display["g9"]+"  |  "+board_cpu_display["g10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" H |  "+board_cpu_display["h1"]+"  |  "+board_cpu_display["h2"]+"  |  "+board_cpu_display["h3"]+"  |  "+board_cpu_display["h4"]+"  |  "+board_cpu_display["h5"] +
          "  |  " + board_cpu_display["h6"]+"  |  "+board_cpu_display["h7"]+"  |  "+board_cpu_display["h8"]+"  |  "+board_cpu_display["h9"]+"  |  "+board_cpu_display["h10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" I |  "+board_cpu_display["i1"]+"  |  "+board_cpu_display["i2"]+"  |  "+board_cpu_display["i3"]+"  |  "+board_cpu_display["i4"]+"  |  "+board_cpu_display["i5"] +
          "  |  " + board_cpu_display["i6"]+"  |  "+board_cpu_display["i7"]+"  |  "+board_cpu_display["i8"]+"  |  "+board_cpu_display["i9"]+"  |  "+board_cpu_display["i10"]+"  ")
    print(hor_vert)
    print(vert)
    print(" J |  "+board_cpu_display["j1"]+"  |  "+board_cpu_display["j2"]+"  |  "+board_cpu_display["j3"]+"  |  "+board_cpu_display["j4"]+"  |  "+board_cpu_display["j5"] +
          "  |  " + board_cpu_display["j6"]+"  |  "+board_cpu_display["j7"]+"  |  "+board_cpu_display["j8"]+"  |  "+board_cpu_display["j9"]+"  |  "+board_cpu_display["j10"]+"  ")
    print(hor_vert)
