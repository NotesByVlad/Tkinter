### Button (Click Action) ###

import tkinter as tk  # Import the Tkinter library

# Function to be called when the button is clicked
def on_button_click():
    print("Button clicked!")  # Print message to the console

# Create the main application window
root = tk.Tk()
root.title("Button Example")  # Set the window title

# Create a Button widget with text and command function
button = tk.Button(root, text="Click Me", font=("Arial", 12), command=on_button_click)

button.pack(pady=10)  # Pack the button into the window with vertical padding

root.mainloop()  # Start the Tkinter event loop