### Label (Text Display) ###

import tkinter as tk         # Import the Tkinter library

# Create the main application window
root = tk.Tk()
root.title("Label Example")  # Set the window title

# Create a Label widget with text, font size, padding
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14), padx=10, pady=10)

label.pack()     # Pack the label into the window (automatic positioning)

root.mainloop()  # Start the Tkinter event loop (keeps the window open)