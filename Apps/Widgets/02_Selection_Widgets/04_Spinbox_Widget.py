### Spinbox Widget (Number Selector) ###

import tkinter as tk  # Import Tkinter

# Function to print the selected value
def show_value():
    print(f"Selected value: {spinbox.get()}")

# Create the main application window
root = tk.Tk()
root.title("Spinbox Example")  # Set the window title

# Create a Spinbox widget (number selector)
spinbox = tk.Spinbox(root, from_=1, to=10)  # Select numbers between 1 and 10

spinbox.pack(pady=10)  # Pack the spinbox into the window

# Create a button to show selected value
button = tk.Button(root, text="Get Value", command=show_value)

button.pack(pady=5)  # Pack the button into the window

root.mainloop()  # Start the Tkinter event loop