### Scale Widget (Slider) ###

import tkinter as tk  # Import Tkinter

# Function to print the slider value
def show_value(value):
    print(f"Slider Value: {value}")

# Create the main application window
root = tk.Tk()
root.title("Scale Example")  # Set the window title

# Create a Scale widget (slider)
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300, command=show_value)

scale.pack(pady=10)  # Pack the scale into the window

root.mainloop()  # Start the Tkinter event loop