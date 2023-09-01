import math

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
            if j < 2:
                print("|", end=" ")
        print("\n", end="")
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O):
        return evaluate(board)

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, 9, float("-inf"), float("inf"), False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i+1, j+1)
    return best_move

def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    while not is_board_full(board):
        print_board(board)
        row, col = get_best_move(board)
        board[row-1][col-1] = PLAYER_X
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("AI wins!")
            return
        elif is_board_full(board):
            break

        print_board(board)
        while True:
            try:
                row = int(input("Enter row (1, 2, or 3): "))
                col = int(input("Enter column (1, 2, or 3): "))
                if board[row-1][col-1] == EMPTY:
                    board[row-1][col-1] = PLAYER_O
                    break
                else:
                    print("Cell already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if check_winner(board, PLAYER_O):
            print_board(board)
            print("AI wins!")
            return

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
