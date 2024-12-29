import pytest
from project import create_board, drop_disc, check_winner

def test_create_board():
    """
    Test the create_board function to ensure it initializes a board correctly.
    """
    board = create_board(6, 7)
    assert len(board) == 6  # Check number of rows
    assert len(board[0]) == 7  # Check number of columns
    assert all(cell == "-" for row in board for cell in row)  # Check all cells are empty


def test_drop_disc():
    """
    Test the drop_disc function to ensure discs are placed correctly.
    """
    board = create_board(6, 7)
    assert drop_disc(board, 0, "R") is True  # Drop in an empty column
    assert board[5][0] == "R"  # Check the disc is at the bottom
    assert drop_disc(board, 0, "Y") is True  # Drop in the same column
    assert board[4][0] == "Y"  # Check the disc is stacked
    full_column = [drop_disc(board, 0, "R") for _ in range(4)]
    assert all(full_column)  # Fill the column
    assert drop_disc(board, 0, "Y") is False  # Column is now full


def test_check_winner():
    """
    Test the check_winner function to ensure it correctly identifies winners.
    """
    board = create_board(6, 7)

    # Test horizontal win
    for i in range(4):
        board[5][i] = "R"
    assert check_winner(board) == "R"

    # Test vertical win
    board = create_board(6, 7)
    for i in range(4):
        board[5 - i][0] = "Y"
    assert check_winner(board) == "Y"

    # Test diagonal (\) win
    board = create_board(6, 7)
    for i in range(4):
        board[5 - i][i] = "R"
    assert check_winner(board) == "R"

    # Test diagonal (/) win
    board = create_board(6, 7)
    for i in range(4):
        board[i][i] = "Y"
    assert check_winner(board) == "Y"
