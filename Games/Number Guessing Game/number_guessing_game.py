import tkinter as tk
from tkinter import ttk, Label, Button, Entry, END, DISABLED, NORMAL, font
import random


class GameApp:
	def __init__(self, root):
		# Initialize main game window
		self.root = root  # Store the passed Tk instance
		self.root.config(bg='#262626')  # Set background color
		self.root.title("Number Guessing Game")  # Set window title
		self.root.geometry("488x380")  # Set window size

		# Define button font style
		self.button_font = font.Font(family="Terminal", size=20)

		# Variables
		self.numbers_range = list(range(1, 9999 + 1))  # Define the number range
		self.selected_range = 0  # Store selected range
		self.tries = 0  # Count number of tries
		self.random_number = None  # Store the random number

		# Title Label
		self.game_title_label = Label(root, text="NUMBER GUESSING GAME", font=("Terminal", 25),
		                              background="#262626", foreground="#b56d43")
		self.game_title_label.grid(row=0, column=0, columnspan=2, sticky="w")

		# Labels for range selection
		self.from_number_label = Label(root, text='FROM 1', font=("Terminal", 20),
		                               background="#262626", foreground="#b56d43")
		self.from_number_label.grid(row=4, column=0, columnspan=1, sticky="w")

		self.until_number_label = Label(root, text='TILL ????', font=("Terminal", 20),
		                                background="#262626", foreground="#b56d43")
		self.until_number_label.grid(row=4, column=1, columnspan=1)

		# Label for tracking tries
		self.tries_label = Label(root, text='TRIES:  ', font=("Terminal", 20),
		                         background="#262626", foreground="#b56d43")
		self.tries_label.grid(row=2, column=0, columnspan=1, sticky="w")

		# Label for game advice and instructions
		self.advice_label = Label(root, text='SELECT THE RANGE NUMBER', font=("Terminal", 20),
		                          background="#262626", foreground="#b56d43")
		self.advice_label.grid(row=6, column=0, columnspan=3)

		# Input Entry (disabled initially)
		self.entry = Entry(root, font=("Terminal", 30), background="#262626", foreground="#b56d43",
		                   width=5, state=DISABLED)
		self.entry.grid(row=3, column=0, columnspan=2, sticky="we")

		# Guess Button
		self.guess = Button(root, text="GUESS", font=self.button_font,
		                    background="#262626", foreground="#b56d43",
		                    command=self.guess_number, width=20, height=2)
		self.guess.grid(row=5, column=0, columnspan=2, sticky="we")

		# Restart Button
		self.restart_button = Button(root, text="RESTART", font=self.button_font,
		                             background="#262626", foreground="#b56d43",
		                             command=self.restart_game, width=10, height=1)
		self.restart_button.grid(row=1, column=1, columnspan=1, sticky="e")

		# Dropdown (ComboBox) for range selection
		self.combo = ttk.Combobox(root, font=("Terminal", 15), values=self.numbers_range)
		self.combo.set("Select the range")  # Default text
		self.combo.bind("<<ComboboxSelected>>", self.select_range)  # Event binding
		self.combo.grid(row=1, column=0, sticky="w")

		# Bind Enter key to guess function
		self.root.bind('<Return>', lambda event: self.guess_number())

	def select_range(self, event):
		# Reset entry field
		self.entry.delete(0, END)

		# Get selected range from ComboBox
		selected_range = self.combo.get()
		self.selected_range = int(selected_range)

		# Reset variables
		self.tries = 0
		self.tries_label.config(text='TRIES:  ')
		self.advice_label.config(text='TYPE YOUR GUESS')

		# Start the game
		self.start_game()

	def start_game(self):
		# Update range labels
		self.from_number_label.config(text="FROM 1")
		self.until_number_label.config(text=f"TILL {self.selected_range}")

		# Generate a random number within the selected range
		self.random_number = random.randint(1, self.selected_range)

		# Enable entry field
		self.entry.config(state=NORMAL)

	def guess_number(self):
		try:
			# Get user input and convert to integer
			number = int(self.entry.get())
		except ValueError:
			# Handle invalid input
			self.entry.delete(0, END)
			self.advice_label.config(text="Please enter a valid number!")
			return

		# Compare input number with random number
		if number > self.random_number:
			self.tries += 1
			self.tries_label.config(text=f"TRIES: {self.tries}")
			self.advice_label.config(text=f"{number} is Too High")
		elif number < self.random_number:
			self.tries += 1
			self.tries_label.config(text=f"TRIES: {self.tries}")
			self.advice_label.config(text=f"{number} is Too Low")
		elif number == self.random_number:
			# Correct guess scenario
			self.entry.delete(0, END)
			self.entry.config(state=DISABLED)
			self.advice_label.config(text=f"\n{number} IS THE NUMBER!")

		# Clear entry field for next input
		self.entry.delete(0, END)

	def restart_game(self):
		# Reset game state
		self.tries = 0
		self.tries_label.config(text="TRIES:  ")
		self.advice_label.config(text="SELECT THE RANGE NUMBER")
		self.entry.delete(0, END)
		self.entry.config(state=DISABLED)
		self.combo.set("Select the range")
		self.until_number_label.config(text="TILL ????")


# Main program execution
if __name__ == "__main__":
	root = tk.Tk()  # Create the Tkinter window instance
	app = GameApp(root)  # Pass instance to the GameApp class
	root.mainloop()  # Start the GUI event loop
