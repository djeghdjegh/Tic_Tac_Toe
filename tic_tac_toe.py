import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'TIE': 0}

    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'O'
            eval = minimax(board_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'X'
            eval = minimax(board_copy, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')

    for i, j in get_empty_cells(board):
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = 'O'
        move_eval = minimax(board_copy, 0, False)

        if move_eval > best_eval:
            best_eval = move_eval
            best_move = (i, j)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already occupied. Try again.")
            continue

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'O'

        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
