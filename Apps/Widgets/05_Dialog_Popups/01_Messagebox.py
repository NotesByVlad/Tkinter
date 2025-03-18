### Messagebox (Popup Alerts) ###

import tkinter as tk  # Import the Tkinter library
from tkinter import messagebox  # Import messagebox module

# Function to show an info messagebox
def show_message():
    messagebox.showinfo("Information", "This is a messagebox!")  # Display an alert popup

# Create the main application window
root = tk.Tk()
root.title("Messagebox Example")  # Set the window title

# Create a button to trigger the messagebox
button = tk.Button(root, text="Show Message", command=show_message)

button.pack(pady=10)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop