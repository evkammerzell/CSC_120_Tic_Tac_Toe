line1 = ['-', '-', '-']
line2 = ['-', '-', '-']
line3 = ['-', '-', '-']
lines = [line1, line2, line3]
locations = {'A1': line1[0], '1A': line1[0], 'B1': line1[1], '1B': line1[1], 'C1': line1[0], '1C': line1[2],
             'A2': line2[0], '2A': line2[0], 'B2': line2[1], '2B': line2[1], 'C2': line2[0], '2C': line2[2],
             'A3': line3[0], '3A': line3[0], 'B3': line3[1], '3B': line3[1], 'C3': line3[0], '3C': line3[2], }


def print_board():
    print("  A B C")
    y = 1
    for x in lines:
        print(str(y), " ".join(x))
        y += 1


def turn(player, symbol):
    print_board()
    move = input(f"Player {player} ({symbol}), enter your move: ")
    while move.upper() not in locations.keys() or locations[move.upper()] != "-":
        if move.upper() not in locations.keys():
            move = input("Please enter a valid location (e.g., A1, B2, C3): ")
        if locations[move.upper()] != "-":
            move = input("Please choose a space not already taken: ")
    locations[move.upper()] = symbol


def play():
    game = True
    while game:
        turn("1", "X")
        turn("2", "O")


play()
