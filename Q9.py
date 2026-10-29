#9. Write a program to implement Tic-Tac-Toe Game.


def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("---+---+---")


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def play_tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a position (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(move) - 1
        if board[position] != ' ':
            print("That position is already taken.")
            continue

        board[position] = current_player

        result = winner(board)
        if result:
            print_board(board)
            print(f"Player {result} wins!")
            break

        if all(cell != ' ' for cell in board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
