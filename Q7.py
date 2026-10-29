#7. Write a program to solve the 8-Queens Problem


def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve_queens(board, row=0):
    n = len(board)
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1

    return False


def print_board(board):
    n = len(board)
    for r in range(n):
        row = []
        for c in range(n):
            row.append('Q' if board[r] == c else '.')
        print(' '.join(row))


if __name__ == "__main__":
    n = int(input("Enter board size (default 8): ") or 8)
    board = [-1] * n
    if solve_queens(board):
        print(f"One valid arrangement for {n} queens:")
        print_board(board)
    else:
        print("No solution exists.")
