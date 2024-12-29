    # Connect_Four_Game
    #### Video Demo:  https://youtu.be/m1EU5eDEMrw
    #### Description: This is a Python implementation of the classic Connect Four game.


--------------------------------------------------------------------------------------------------------


### CONNECT FOUR GAME - PYTHON IMPLEMENTATION ###

The project is built as part of a programming assignment from CS50P course FINAL PROJECT and adheres to specific requirements, including modular code design, testing with pytest, and proper structure for ease of use.

--------------------------------------------------------------------------------------------------------


### WHAT IS CONNECT FOUR GAME? ###

    Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a game in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. It is therefore a type of m,n,k-game (7, 6, 4) with restricted piece placement. Connect Four is a solved game. The first player can always win by playing the right moves.

    The game was created by Howard Wexler, and first sold under the Connect Four trademark[10] by Milton Bradley in February 1974.

    Object: Connect four of your discs in a row while preventing your opponent from doing the same.
    But, look out – your opponent can sneak up on you and win the game!

    — Milton Bradley, Connect Four "Pretty Sneaky, Sis" television commercial, 1977
    -- Wikipedia --


--------------------------------------------------------------------------------------------------------


### Project Features ###

	--Interactive Gameplay
        Players take turns to drop discs in a 6x7 grid.
	--Winning Conditions
        game detects horizontal, vertical, and diagonal wins.
	--Draw Detection
        Game ends in a draw if the board is completely filled without a winner.
	--Modular Code
        Key functionalities are implemented in separate functions.
    --Testing
        Includes test cases written with pytest to validate core functionalities.(test_project.py)


--------------------------------------------------------------------------------------------------------


### How to Play ###

	RED starts with the color R (Red).
	YELLOW follows with the color Y (Yellow).
	Players take turns choosing a column to drop their disc. ( STARTS FROM 0)
	The first player to align four discs horizontally, vertically, or diagonally wins.
	If the board is filled without a winner, the game ends in a draw.

--------------------------------------------------------------------------------------------------------

### PROJECT.PY: ###
    main(): Runs the game loop and handles player interactions.
	create_board(rows, cols): Initializes the game board.
	drop_disc(board, col, color): Simulates a player’s move by dropping a disc in the specified column.
	check_winner(board): Checks the board for any winning condition.


### TEST_PROJECT.PY. ###
	create_board(): test init of board.
	drop_disc(): Verify that discs are placed correctly in the grid.
	check_winner(): Tests all possible winning scenarios
        -horizontal
        -vertical
        -diagonal


--------------------------------------------------------------------------------------------------------



### GAME PLAY EXAMPLE ###

Welcome to Connect Four!
Player 1's turn (R).
Choose a column (0-6): 3

- - - - - - -
- - - - - - -
- - - - - - -
- - - - - - -
- - - - - - -
- - - R - - -
0 1 2 3 4 5 6 (COL NUMBERS)

----------------------------->

Player 2's turn (Y).
Choose a column (0-6): 2

- - - - - - -
- - - - - - -
- - - - - - -
- - - - - - -
- - - - - - -
- - Y R - - -

----------------------------->

Welcome to Connect Four!
Player 1's turn (R).
Choose a column (0-6): 3

- - - - - - -
- - - - - - -
- - - - - - -
- - - - - - -
- - - R - - -
- - Y R - - -



----------------
FILE STRUCTURE ->

project/
|
|-- project.py
|-- test_project.py
|-- README.md

------------------------------THANK YOU---------------------------
@fatihoezkan
