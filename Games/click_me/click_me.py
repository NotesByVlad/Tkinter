import tkinter as tk
from tkinter import ttk, Label, Button, font
import random


class GameApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.config(bg='#262626')  # Set background color
        self.root.title("Click the Button Game")  # Set window title
        self.root.geometry("500x500")  # Set window size
        self.root.resizable(False, False)  # Prevent resizing

        # Define style for text
        self.terminal_font = font.Font(family="Terminal", size=15)

        # Variables to manage game state
        self.seconds = [10, 20, 30, 40, 50]  # Possible timer values
        self.click_count = 0  # Number of clicks made by the player
        self.time_left = 10  # Time left for the current game
        self.timer_running = False  # Flag to check if timer is running
        self.timer_id = None  # Variable to store timer ID for cancellation

        # Labels for instructions, click count, and timer
        self.instruction_label = Label(root, text="To start the game, click the button",
                                       bg="#262626", fg="#b56d43", font=self.terminal_font)
        self.instruction_label.place(x=0, y=0)  # Position label in the window

        self.count_label = Label(root, text="Clicks: 0",
                                 bg="#262626", fg="#b56d43", font=self.terminal_font)
        self.count_label.place(x=250, y=30)  # Position label in the window

        self.timer_label = Label(root, text="Time: ",
                                 bg="#262626", fg="#b56d43", font=self.terminal_font)
        self.timer_label.place(x=400, y=30)  # Position label in the window

        # Dropdown (ComboBox) for selecting timer duration
        self.combo = ttk.Combobox(root, font=self.terminal_font,
                                   values=[str(sec) for sec in self.seconds])
        self.combo.set("Timer")  # Default text in the ComboBox
        self.combo.bind("<<ComboboxSelected>>", self.select_seconds)  # Event binding for selection
        self.combo.place(x=0, y=30)  # Position ComboBox in the window

        # Button for clicking action
        self.click_button = Button(root, text="Click Me!",
                                   bg="#262626", fg="#b56d43",
                                   font=self.terminal_font, command=self.switch_place)
        self.click_button.place(x=250, y=250)  # Position button in the window

        # Reset button to restart the game
        self.reset_button = Button(root, text="Reset",
                                   bg="#262626", fg="#b56d43",
                                   font=self.terminal_font, command=self.reset_game)
        self.reset_button.place(x=400, y=0)  # Position Reset button in the window

    def select_seconds(self, event):
        # Called when a new time is selected from the ComboBox
        selected_time = self.combo.get()  # Get selected value from ComboBox

        # Convert selected value to integer if it's a digit
        if selected_time.isdigit():
            self.time_left = int(selected_time)  # Convert to int
        else:
            self.time_left = 10  # Default time if no valid selection

        # Update the timer label with the new time
        self.timer_label.config(text=f"Time: {self.time_left}")
        self.reset_game()  # Reset game when time is changed

    def switch_place(self):
        # Called when the click button is pressed
        if not self.timer_running:  # Check if the timer isn't running
            self.timer_running = True  # Set timer_running flag to True
            self.combo.config(state='disabled')  # Disable time selection during gameplay
            self.start_timer()  # Start the timer

        # Move the click button to a random position
        new_x = random.randint(10, 450)
        new_y = random.randint(50, 450)

        self.click_count += 1  # Increment click count
        self.click_button.place(x=new_x, y=new_y)  # Move button to new position

        # Update click count display label
        self.count_label.config(text=f"Clicks: {self.click_count}")

    def start_timer(self):
        # Timer function that counts down
        if self.time_left > 0:  # Check if time is remaining
            self.timer_id = self.root.after(1000, self.start_timer)  # Schedule next timer tick
            self.time_left -= 1  # Decrease time left
            self.timer_label.config(text=f"Time: {self.time_left}")  # Update timer display
        else:
            # Actions when time runs out
            self.click_button.config(state='disabled')  # Disable click button
            self.instruction_label.config(text="Time's up! Game Over")  # Update instruction label
            self.combo.config(state='normal')  # Enable time selection again
            self.timer_running = False  # Reset the running state

    def reset_game(self):
        # Reset game state and UI components
        self.click_count = 0  # Reset click counter
        self.count_label.config(text="Clicks: 0")  # Update click display
        self.click_button.config(state='normal')  # Re-enable the click button
        self.combo.config(state='normal')  # Re-enable time selection
        self.instruction_label.config(text="To start the game click the button")  # Reset instructions

        # Stop the timer if it's running
        if self.timer_running:
            self.root.after_cancel(self.timer_id)  # Cancel the timer
            self.timer_running = False  # Reset running state

        # Reset timer based on selected value or to default if none is selected
        self.time_left = int(self.combo.get()) if self.combo.get().isdigit() else 10
        self.timer_label.config(text=f"Time: {self.time_left}")  # Update timer display


# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create a Tkinter window instance
    app = GameApp(root)  # Pass the window to the GameApp class
    root.mainloop()  # Start the GUI event loop