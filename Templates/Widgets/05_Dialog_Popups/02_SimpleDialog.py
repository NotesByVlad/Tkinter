### SimpleDialog (User Prompt) ###

import tkinter as tk  # Import the Tkinter library
from tkinter import simpledialog  # Import simpledialog module

# Function to ask for user input via dialog
def ask_name():
    name = simpledialog.askstring("Input", "What is your name?")  # Show input dialog
    if name:  # If user provided a name
        print(f"User entered: {name}")  # Print the name

# Create the main application window
root = tk.Tk()
root.title("SimpleDialog Example")  # Set the window title

# Create a button to open the input dialog
button = tk.Button(root, text="Enter Name", command=ask_name)

button.pack(pady=10)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop