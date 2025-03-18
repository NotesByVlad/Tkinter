from tkinter import *  # Import all the tkinter module for GUI components

class GameApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root  # Assign the root window (Tkinter window)
        self.root.config(bg='#262626')  # Set background color of the window
        self.root.title("Tic Tac Toe")  # Set the title of the window
        self.root.geometry("348x500")  # Set the size of the window
        self.root.resizable(False, False)  # Disable resizing of the window

        # Styling
        self.x_color ="#4287f5"  # Define color for player X
        self.o_color ="#e6253b"  # Define color for player O
        self.current_color = self.x_color  # Set the initial color for player X

        # Variables to hold the players' symbols, scores, etc.
        self.x = "X"  # Player X's symbol
        self.o = "O"  # Player O's symbol
        self.x_score = 0  # Initialize X's score to 0
        self.o_score = 0  # Initialize O's score to 0
        self.turns = 0  # Track the number of turns
        self.game_over = False  # Flag to check if the game is over

        self.current_player = self.x  # Set the initial player to X
        self.starting_player = self.x  # Set the initial starting player to X

        # Upper frame to hold the score and buttons
        self.labels = LabelFrame(root, bg="#262626")  # Create a frame for scores
        self.labels.grid(row=0, column=0, columnspan=5)  # Place it at the top (row 0)

        # Board frame to hold the Tic Tac Toe grid
        self.board = LabelFrame(root, bg="#262626")  # Create a frame for the board
        self.board.grid(row=1, column=0)  # Place the board below the score frame

        # Labels to display the scores for X and O
        self.x_score_label = Label(self.labels, text="X: ", bg="#262626", fg="#ffffff", width=4, height=1,
                                   font=("Helvetica", 20))  # Create label for X score
        self.x_score_label.grid(row=0, column=0, sticky="w", padx=3)  # Position X score label

        self.o_score_label = Label(self.labels, text="O: ", bg="#262626", fg="#ffffff", width=4, height=1,
                                   font=("Helvetica", 20))  # Create label for O score
        self.o_score_label.grid(row=0, column=2, sticky="e", padx=3)  # Position O score label

        ## Buttons
        # Next round Button to reset the game after it ends
        self.play_next_button = Button(self.labels, width=10, height=1, text="Next Round", state=DISABLED,
                                       bg="#262626", fg="#ffffff", font=("Helvetica", 10),
                                        command=lambda: self.next_round())  # Call next_round method when clicked
        self.play_next_button.grid(row=0, column=1)  # Position the "Next Round" button

        # Board Buttons (buttons for the Tic Tac Toe grid)
        self.buttons = [[], [], []]  # 3x3 list to store buttons

        # Loop through each row and column to create 9 buttons for the Tic Tac Toe grid
        for row in range(3):
            for column in range(3):
                button = Button(self.board, font=("Helvetica", 20), width=6, height=3, bg="#262626",
                                pady=5, padx=5,
                                command=lambda r=row, c=column: self.click(r, c))  # Call click method when clicked
                button.grid(row=row, column=column)  # Place the button in the grid
                self.buttons[row].append(button)  # Add the button to the 2D list of buttons

    ## Methods
    def click(self, row, column):
        # Mark Tile
        self.buttons[row][column].config(text=self.current_player, 
                                         fg=self.current_color,  # Set text color
                                         disabledforeground=self.current_color)  # Set text color when disabled
        self.change_player()  # Switch to the next player
        self.change_colors()  # Change the color for the next player
        self.disable_buttons(row, column)  # Disable the clicked button
        self.check_winner(row, column)  # Check if there's a winner after each move

    def change_player(self):  # Change the current player after a move
        self.current_player = self.o if self.current_player == self.x else self.x  # Switch player
        self.turns += 1  # Increment the number of turns

    def change_colors(self):  # Switch color for the next player
        if self.current_color == self.x_color:  # If current player is X
            self.current_color = self.o_color  # Switch to O's color
            self.o_score_label.config(fg=self.o_color)  # Set O score label to O's color
            self.x_score_label.config(fg="#ffffff")  # Set X score label to default color
        else:  # If current player is O
            self.current_color = self.x_color  # Switch to X's color
            self.x_score_label.config(fg=self.x_color)  # Set X score label to X's color
            self.o_score_label.config(fg="#ffffff")  # Set O score label to default color

    def disable_buttons(self, row=None, column=None):
        # Disable a single button
        if row is not None and column is not None:
            self.buttons[row][column].config(state=DISABLED)  # Disable clicked button
        # Disable all buttons
        else:
            for row in self.buttons:
                for button in row:
                    button.config(state=DISABLED)  # Disable all buttons

    def enable_buttons(self):
        # Enable all buttons and reset text to empty
        for row in self.buttons:
            for button in row:
                button.config(state=NORMAL, text="", bg="#262626")  # Enable and reset button state

    def check_winner(self, r, c):
        btn = self.buttons  # Reference the buttons 2D list
        # Check if any row is complete
        if btn[r][0]['text'] == btn[r][1]['text'] == btn[r][2]['text'] != '':
            self.win_settings()  # Call win settings if a row is complete
            for i in range(3):
                btn[r][i].config(bg="#121212",  disabledforeground="#ffffff")  # Highlight the winning row

        # Check if any column is complete
        elif btn[0][c]['text'] == btn[1][c]['text'] == btn[2][c]['text'] != '':
            self.win_settings()  # Call win settings if a column is complete
            for i in range(3):
                btn[i][c].config(bg="#121212",  disabledforeground="#ffffff")  # Highlight the winning column

        # Check if the first diagonal is complete
        elif btn[0][0]['text'] == btn[1][1]['text'] == btn[2][2]['text'] != '':
            self.win_settings()  # Call win settings if the first diagonal is complete
            for i in range(3):
                btn[i][i].config(bg="#121212",  disabledforeground="#ffffff")  # Highlight the first diagonal

        # Check if the anti-diagonal is complete
        elif btn[0][2]['text'] == btn[1][1]['text'] == btn[2][0]['text'] != '':
            self.win_settings()  # Call win settings if the anti-diagonal is complete
            for i in range(3):
                btn[i][2-i].config(bg="#121212",  disabledforeground="#ffffff")  # Highlight the anti-diagonal

        # Check if all cells are filled (draw scenario)
        elif self.turns == 9:
            self.game_over = True  # Set game as over
            self.play_next_button.config(state=NORMAL)  # Enable the "Next Round" button

    def win_settings(self):
        self.update_score()  # Update the score after a win
        self.game_over = True  # Set game as over
        self.disable_buttons()  # Disable all buttons
        self.starting_player_func()  # Determine the new starting player for the next round
        self.play_next_button.config(state=NORMAL)  # Enable the "Next Round" button

    def update_score(self):
        if self.current_player == self.o:  # If O won
            self.x_score += 1  # Increment X's score
            self.x_score_label.config(text=f"X: {self.x_score}")  # Update X's score label
        else:  # If X won
            self.o_score += 1  # Increment O's score
            self.o_score_label.config(text=f"O: {self.o_score}")  # Update O's score label

    def next_round(self):
        if self.game_over:  # If the game is over
            self.game_over = False  # Set game over flag to False for the new round
            self.turns = 0  # Reset the number of turns
            self.play_next_button.config(state=DISABLED)  # Disable the "Next Round" button
            self.enable_buttons()  # Enable all buttons for the next round

    def starting_player_func(self):
        self.starting_player = self.o if self.starting_player == self.x else self.x  # Switch starting player
        self.current_player = self.starting_player  # Set current player to the new starting player

# Main program execution
if __name__ == "__main__":
    root = Tk()  # Create a Tkinter window instance
    app = GameApp(root)  # Create an instance of the GameApp class
    root.mainloop()  # Start the GUI event loop