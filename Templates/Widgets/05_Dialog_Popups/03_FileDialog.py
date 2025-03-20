### FileDialog (Open/Save File Dialogs) ###

import tkinter as tk  # Import Tkinter
from tkinter import filedialog  # Import file dialog module

# Function to open a file dialog
def open_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        print(f"Selected file: {file_path}")

# Create the main application window
root = tk.Tk()
root.title("FileDialog Example")  # Set the window title

# Create a button to open file dialog
button = tk.Button(root, text="Open File", command=open_file)
button.pack(pady=10)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop