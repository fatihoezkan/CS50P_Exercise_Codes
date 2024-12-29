def main():
    """
    Main function to play the Connect Four game.
    """
    rows, cols = 6, 7
    board = create_board(rows, cols)

    current_player = 1
    colors = {1: "R", 2: "Y"}

    print("Welcome to Connect Four!")
    while True:
        print(f"Player {current_player}'s turn ({colors[current_player]}).")
        try:
            col = int(input(f"Choose a column (0-{cols - 1}): "))
            if col < 0 or col >= cols:
                print("Invalid column. Try again.")
                continue

            if not drop_disc(board, col, colors[current_player]):
                print("Column is full. Try a different column.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Print the board
        for row in board:
            print(" ".join(row))
        print()

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print(f"Player {current_player} ({winner}) wins!")
            break

        # Check for a draw
        if all(cell != "-" for row in board for cell in row):
            print("The game is a draw!")
            break

        # Switch player
        current_player = 1 if current_player == 2 else 2

    print("Game Over.")


def create_board(rows=6, cols=7):
    """
    Create an empty board with specified rows and columns.
    """
    return [["-" for _ in range(cols)] for _ in range(rows)]


def drop_disc(board, col, color):
    """
    Drop a disc of the given color into the specified column.
    Returns True if the move is successful, False if the column is full.
    """
    for row in reversed(board):  # Start checking from the bottom
        if row[col] == "-":
            row[col] = color
            return True
    return False


def check_winner(board):
    """
    Check all possible win conditions: horizontal, vertical, and diagonal.
    Returns the color of the winner or None if there's no winner yet.
    """
    rows, cols = len(board), len(board[0])

    # Check horizontal wins
    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] != "-" and all(board[row][col] == board[row][col + i] for i in range(4)):
                return board[row][col]

    # Check vertical wins
    for col in range(cols):
        for row in range(rows - 3):
            if board[row][col] != "-" and all(board[row][col] == board[row + i][col] for i in range(4)):
                return board[row][col]

    # Check diagonal (\) wins
    for row in range(3, rows):
        for col in range(cols - 3):
            if board[row][col] != "-" and all(board[row][col] == board[row - i][col + i] for i in range(4)):
                return board[row][col]

    # Check diagonal (/) wins
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] != "-" and all(board[row][col] == board[row + i][col + i] for i in range(4)):
                return board[row][col]

    return None  # No winner yet



if __name__ == "__main__":
    main()
