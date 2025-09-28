# Tic Tac Toe Game in Python

board = [" "] * 9

def print_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def tic_tac_toe():
    current_player = "X"
    moves = 0

    while True:
        print_board()
        try:
            pos = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input, enter a number between 1-9.")
            continue

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid move, try again!")
            continue

        board[pos] = current_player
        moves += 1

        if check_win(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if moves == 9:
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()