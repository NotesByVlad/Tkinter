### Radiobutton Widget (Single Selection) ###

import tkinter as tk  # Import Tkinter

# Function to display selected option
def show_choice():
    print(f"Selected option: {var.get()}")

# Create the main application window
root = tk.Tk()
root.title("Radiobutton Example")  # Set the window title

# Create an IntVar to store selected option
var = tk.IntVar(value=1)  # Default selection is option 1

# Create Radiobutton widgets
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=show_choice)
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=show_choice)

radio1.pack(pady=2)  # Pack the first radio button
radio2.pack(pady=2)  # Pack the second radio button

root.mainloop()  # Start the Tkinter event loop