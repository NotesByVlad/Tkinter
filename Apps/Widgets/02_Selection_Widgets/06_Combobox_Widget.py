### Combobox Widget (Dropdown Selection) ###

import tkinter as tk  # Import Tkinter
from tkinter import ttk  # Import themed widgets

# Function to print the selected item
def show_selection(event):
    print(f"Selected item: {combobox.get()}")

# Create the main application window
root = tk.Tk()
root.title("Combobox Example")  # Set the window title

# Create a Combobox widget
combobox = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])  # List of options

combobox.pack(pady=10)  # Pack the combobox into the window

# Bind selection event
combobox.bind("<<ComboboxSelected>>", show_selection)

root.mainloop()  # Start the Tkinter event loop