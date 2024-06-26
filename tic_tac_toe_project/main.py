import math

# Define the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    print("\n")

# Check for a win
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Check for a tie
def is_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Get available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Map user input to board coordinates
def map_input_to_coordinates(user_input):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return mapping.get(user_input)

# Main game loop
def play_game():
    board = initialize_board()
    human = 'X'
    ai = 'O'
    current_player = human

    while True:
        print_board(board)
        if current_player == human:
            user_input = int(input("Enter your move (1-9): "))
            move = map_input_to_coordinates(user_input)
            if move and board[move[0]][move[1]] == ' ':
                board[move[0]][move[1]] = human
                if check_winner(board, human):
                    print_board(board)
                    print("You win!")
                    break
                current_player = ai
            else:
                print("Invalid move. Try again.")
        else:
            move = get_best_move(board)
            board[move[0]][move[1]] = ai
            if check_winner(board, ai):
                print_board(board)
                print("AI wins!")
                break
            current_player = human

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

play_game()
