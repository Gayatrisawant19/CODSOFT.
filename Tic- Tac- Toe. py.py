import math

# Function to display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the current board state is a win for a player
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i] == [player, player, player]:  # Check rows
            return True
        if [board[j][i] for j in range(3)] == [player, player, player]:  # Check columns
            return True

    # Check diagonals
    if [board[i][i] for i in range(3)] == [player, player, player]:
        return True
    if [board[i][2 - i] for i in range(3)] == [player, player, player]:
        return True

    return False

# Function to check if the game is a draw
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to evaluate the score (1 for AI win, -1 for human win, 0 for draw)
def evaluate(board):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    else:
        return 0

# Function to check if there are any moves left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If the game has ended, return the score
    if score == 1 or score == -1:
        return score

    # If no more moves left, it's a draw
    if not is_moves_left(board):
        return 0

    # Maximizing player (AI)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'  # AI move
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = " "  # Undo move
        return best_score

    # Minimizing player (Human)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'  # Human move
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = " "  # Undo move
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'  # AI move
                move_score = minimax(board, 0, False)
                board[i][j] = " "  # Undo move

                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)

    return best_move

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human player move
        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken! Choose another.")

        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        move = find_best_move(board)
        board[move[0]][move[1]] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break

        if is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
