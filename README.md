# Tic-Tac-Toe AI using Minimax Algorithm

This project implements an AI to play Tic-Tac-Toe optimally using the Minimax algorithm. The game interface is provided by `main.py`, while the game logic and AI implementation are in `tictactoe.py`.

## Game Overview

In the game of Tic-Tac-Toe, two players take turns marking cells on a 3x3 grid. The first player is X, and the second player is O. The game ends when one player successfully places three of their marks in a row, column, or diagonal, or when all cells on the grid are filled without any player winning.

## Files

- `main.py`: This file contains the code to run the graphical interface for the game. Players can interact with the game through this interface.
- `tictactoe.py`: This file contains all the logic for playing the game and making optimal moves using the Minimax algorithm. It includes functions for determining the current player, available actions, making moves, checking for a winner, determining if the game is over, and evaluating the utility of a terminal board.

## Specification

The project follows the specifications provided by CS50, and completion of the following functions is required:

- `player(board)`: Returns the player who has the next turn on the board.
- `actions(board)`: Returns a set of all possible actions available on the board.
- `result(board, action)`: Returns the board that results from making a move on the board.
- `winner(board)`: Returns the winner of the game if there is one.
- `terminal(board)`: Returns True if the game is over, False otherwise.
- `utility(board)`: Returns the utility value of the board.
- `minimax(board)`: Returns the optimal action for the current player on the board.

## Running the Game

To play against the AI, simply run `python main.py` in your terminal. The graphical interface will allow you to make moves against the AI, and you can see the optimal moves made by the AI using the Minimax algorithm. Since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI, although you may win if you don't play optimally.


## Credits

This project is part of the assignments provided by the CS50AI course, an introduction to Artificial Intelligence with Python offered by Harvard University. The original idea and specifications for implementing the Tic-Tac-Toe AI using the Minimax algorithm are credited to the CS50 team.

The code implementation provided in tictactoe.py and runner.py is based on the guidelines and specifications provided by CS50.
