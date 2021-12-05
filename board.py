line1 = ['-', '-', '-']
line2 = ['-', '-', '-']
line3 = ['-', '-', '-']
winner = ""
player1 = {"Wins": 0, "Losses": 0}
player2 = {"Wins": 0, "Losses": 0}
total = 0
cont = True


def print_board():
    lines = [line1, line2, line3]
    print("  A B C")
    y = 1
    for x in lines:
        print(str(y), " ".join(x))
        y += 1


def turn(player, symbol):
    locations = {'A1': line1[0], '1A': line1[0], 'B1': line1[1], '1B': line1[1], 'C1': line1[2], '1C': line1[2],
                 'A2': line2[0], '2A': line2[0], 'B2': line2[1], '2B': line2[1], 'C2': line2[2], '2C': line2[2],
                 'A3': line3[0], '3A': line3[0], 'B3': line3[1], '3B': line3[1], 'C3': line3[2], '3C': line3[2]}
    print_board()
    move = input(f"Player {player} ({symbol}), enter your move: ")
    while move.upper() not in locations.keys() or locations[move.upper()] != "-":
        if move.upper() not in locations.keys():
            move = input("Please enter a valid location (e.g., A1, B2, C3): ")
        if locations[move.upper()] != "-":
            move = input("Please choose a space not already taken: ")
    mark_board(move.upper(), symbol)


def mark_board(location, symbol):
    if "A" in location:
        spot = 0
    elif "B" in location:
        spot = 1
    else:
        spot = 2
    if "1" in location:
        line1[spot] = symbol
    elif "2" in location:
        line2[spot] = symbol
    elif "3" in location:
        line3[spot] = symbol


def board_check():
    global winner
    checks = [line1, line2, line3, [line1[0], line2[0], line3[0]], [line1[1], line2[1], line3[1]],
              [line1[2], line2[2], line3[2]], [line1[0], line2[1], line3[1]], [line1[2], line2[1], line3[0]]]
    for x in checks:
        if x.count("X") == 3:
            winner = "1"
            return False
        elif x.count("O") == 3:
            winner = "2"
            return False
    if line1.count("-") + line2.count("-") + line3.count("-") == 0:
        winner = "0"
        return False
    return True


def play():
    global total
    game = True
    player = "2"
    symbol = "O"
    while game:
        if player == "2":
            player = "1"
            symbol = "X"
        elif player == "1":
            player = "2"
            symbol = "O"
        turn(player, symbol)
        game = board_check()
    if winner == "1":
        print_board()
        print("Player 1 wins!")
        player1["Wins"] += 1
        player2["Losses"] += 1
    elif winner == "2":
        print_board()
        print("Player 2 wins!")
        player2["Wins"] += 1
        player1["Losses"] += 1
    else:
        print_board()
        print("It's a tie!")
    total += 1


def main():
    global line3, line2, line1, winner, cont
    print("Player 1:")
    print(f'Wins: {player1["Wins"]}, Losses: {player1["Losses"]}')
    print("Player 2:")
    print(f'Wins: {player2["Wins"]}, Losses: {player2["Losses"]}')
    print(f'Total Games: {total}')
    print("Would you like to play a game?")
    choice = input("Enter 'y' for yes or 'n' for no: ")
    while choice not in ['y', 'n']:
        choice = input("Enter 'y' for yes or 'n' for no: ")
    if choice == 'y':
        line1 = ['-', '-', '-']
        line2 = ['-', '-', '-']
        line3 = ['-', '-', '-']
        winner = ""
        play()
    else:
        cont = False


while cont:
    main()
