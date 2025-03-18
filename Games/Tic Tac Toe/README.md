# Tic Tac Toe Game in Python (Tkinter)

This is a simple and interactive Tic Tac Toe game built using Python and the Tkinter library for the graphical user interface (GUI). The game allows two players to play Tic Tac Toe on a 3x3 grid, with the scores displayed at the top of the window. It also supports multiple rounds with score tracking, and automatically switches turns between players.

## Features

- **Two-player mode:** Players can take turns placing "X" and "O" on the grid.
- **Score tracking:** The scores for both players (X and O) are displayed and updated after each round.
- **Next round functionality:** After a round ends (either by win or draw), players can start a new round without restarting the game.
- **Winner highlighting:** Winning rows, columns, or diagonals are highlighted when a player wins.
- **Player turns:** The game alternates between player X (blue) and player O (red).
- **Game over handling:** The game automatically detects the winner or a draw and disables further moves until the next round is initiated.

## Requirements

- Python 3.x
- Tkinter (Usually comes pre-installed with Python)

## How to Run the Game

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/NotesByVlad/Python.git

   ```

2. Navigate to the folder:

   ```bash
   cd Python/Tkinter/Games/Tic\ Tac\ Toe

   ```

3. Run the tic tac toe.py file:
   ```bash
   python "tic tac toe.py"
   ```

## Game Controls

- Player X and Player O will take turns clicking on the empty squares in the 3x3 grid.
- Player X will use the blue color, while Player O will use the red color.
- After a round ends (whether by a win or a draw), click the "Next Round" button to start a new round.

## Game Logic

- The game checks for a win after every move by evaluating rows, columns, and diagonals.
- If a player wins, the winning cells are highlighted, and the score for the winning player is updated.
- The game also handles draws if all cells are filled without a winner.
- Players alternate starting the game, and after each round, the player who did not start the last round becomes the starting player for the next round.

## Acknowledgements

- This game was developed as a fun and simple project using Python and Tkinter.
- Special thanks to the open-source community for creating the tools and documentation that made this project possible.

### Explanation of the Sections:

- **Features**: This section outlines what the game does (e.g., alternating players, score tracking, win condition).
- **Requirements**: Specifies the tools needed to run the game (Python and Tkinter).
- **How to Run the Game**: Instructions to clone and run the game locally.
- **Game Controls**: Describes the user interactions with the game.
- **Game Logic**: Explains how the game detects wins, draws, and alternates between players.
- **License**: Gives information about the licensing of the project (you can change it if you use a different license).
- **Acknowledgements**: Mentions credits to the open-source community.

This README will provide a good overview of your project and help others understand how to run and use it!
