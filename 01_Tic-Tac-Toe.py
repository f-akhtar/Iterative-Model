# Command Line User Interface With Test-Cases
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Enter row (0, 1, 2) for player {current_player}: "))
        col = int(input(f"Enter column (0, 1, 2) for player {current_player}: "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return winner

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return 'Tie'

        current_player = 'O' if current_player == 'X' else 'X'

def run_tests():
    # Test case 1: X wins
    board1 = [['X', 'X', 'X'],
              [' ', 'O', 'O'],
              [' ', ' ', 'O']]
    assert check_winner(board1) == 'X'

    # Test case 2: O wins
    board2 = [['O', 'X', 'X'],
              ['O', 'X', 'O'],
              ['O', ' ', ' ']]
    assert check_winner(board2) == 'O'

    # Test case 3: X wins
    board3 = [['X', 'O', 'O'],
              [' ', 'X', ' '],
              ['O', ' ', 'X']]
    assert check_winner(board3) == 'X'

    # Test case 4: Board is full (Tie)
    board4 = [['X', 'O', 'X'],
              ['X', 'X', 'O'],
              ['O', 'X', 'O']]
    assert is_board_full(board4) == True

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
    play_tic_tac_toe()
